import json

# Load data from JSON files
with open(r"D:\#Codes\HAlloc_django\HAlloc\hostel_allocation\allocation_app\data\students.json", 'r') as f:
    students_data = json.load(f)

with open(r"D:\#Codes\HAlloc_django\HAlloc\hostel_allocation\allocation_app\data\rooms.json", 'r') as f:
    rooms_data = json.load(f)

with open(r"D:\#Codes\HAlloc_django\HAlloc\hostel_allocation\allocation_app\data\preferences.json", 'r') as f:
    preferences_data = json.load(f)

# Initialize data structures
LoginIds = list(students_data.keys())
Id_rank_dict = {student_id: details['rank'] for student_id, details in students_data.items()}
Rank_People_Dict = {student_id: [details['block'], details['room_type']] for student_id, details in students_data.items()}
Block_list = list(rooms_data.keys())
Room_Type_list = [
    ["1_Bed_ac", 2], ["1_Bed_nac", 2], 
    ["2_Bed_ac", 2], ["2_Bed_nac", 2], 
    ["3_Bed_ac", 2], ["3_Bed_nac", 2], 
    ["4_Bed_ac", 2], ["4_Bed_nac", 2], 
    ["6_Bed_ac", 2], ["6_Bed_nac", 2], 
    ["8_Bed_ac", 2], ["8_Bed_nac", 2]
]   # accomodates max 96 people (for now)

# Initialize room availability

Block_Room_Types = {block: {room_type[0]: room_type[1] for room_type in Room_Type_list} for block in Block_list}


left_people_list = []
All_preference = []
chosen_list = []
self_list = []

# Process preferences from JSON
for pref in preferences_data:
    student_id = pref['id']
    pref_no = pref['preference_no']
    block = pref['block']
    room_type = pref['room_type']
    roommates = pref['roommates']
    All_preference.append([student_id, pref_no, block, room_type, roommates])

# def is_room_available(block, room_type):
#     if Block_Room_Types.get(block, {}).get(room_type, 0) > 0:
#         return True
#     return False

def is_room_available(block, room):   #take 2 string input, check from "Block_Room_Types" if avalible, return T/F
    if Block_Room_Types[block][room] > 0:
        return True
    return False

def is_Id_allocated(student_id):     #take 1 string input, check is block/room_type is allocated, return T/F
    if Rank_People_Dict[student_id][0] == "":
        return False
    return True

def sort_all_preferences():     # first sort by rank, then sort by preference number
    All_preference.sort(key=lambda x: (Id_rank_dict.get(x[0], float('inf')), x[1]), reverse=False)

def MasterFunction():   # completes first round of allocations
    for preference in All_preference:
        student_id = preference[0]
        
        if is_Id_allocated(student_id):
            continue

        block = preference[2]
        room_type = preference[3]

        if not is_room_available(block, room_type):
            continue

        if any(is_Id_allocated(pref_id) for pref_id in preference[4]):
            continue

        # Check if all roommates are in the same preference
        # all_roommates_have_same_pref = True
        # for roommate in preference[4]:
        #     roommate_has_pref = False
        #     for pref in All_preference:
        #         if pref[0] == roommate and pref[2] == block and pref[3] == room_type and set(pref[4]) == set(preference[4]):
        #             roommate_has_pref = True
        #             break
        #     if not roommate_has_pref:
        #         all_roommates_have_same_pref = False
        #         break

        # if not all_roommates_have_same_pref:
        #     continue

        # Allocate the room
        for student in preference[4]:
            Rank_People_Dict[student][0] = block
            Rank_People_Dict[student][1] = room_type
        Block_Room_Types[block][room_type] -= 1

def roomless_id_list(): # makes a list of all IDs without a room
    for student_id in LoginIds:
        if not is_Id_allocated(student_id):
            left_people_list.append(student_id)

def secondary_allotment():
    while len(left_people_list) != 0:
        for block in ["A", "B", "C"]: 
            for room_type in ["8_Bed_nac", "8_Bed_ac", "6_Bed_nac", "6_Bed_ac"]:
                if is_room_available(block, room_type):
                    # Calculate how many people we can fit in this room
                    members_per_room = rooms_data[block][room_type]['members_per_room']
                    num_rooms_available = Block_Room_Types[block][room_type]
                    total_capacity = members_per_room * num_rooms_available
                    
                    # Take as many people as we can fit
                    people_to_allocate = left_people_list[:total_capacity]
                    
                    # Allocate them
                    for person in people_to_allocate:
                        Rank_People_Dict[person][0] = block
                        Rank_People_Dict[person][1] = room_type
                    
                    # Update room availability
                    rooms_needed = len(people_to_allocate) // members_per_room
                    if len(people_to_allocate) % members_per_room != 0:
                        rooms_needed += 1
                    Block_Room_Types[block][room_type] -= rooms_needed
                    
                    # Remove allocated people from the list
                    for person in people_to_allocate:
                        left_people_list.remove(person)
                    
                    if not left_people_list:
                        return
                    break

def display():
    for student_id, details in Rank_People_Dict.items():
        print(f"ID - {student_id}, Block - {details[0]}, Room Type - {details[1]}")

def room_taken_in():
    search_id = input("Enter ID to look for : ")
    for i in All_preference:
        if i[0]==search_id:
            self_list.append(i)
            continue

        for j in i[4]:
            if search_id in j:
                chosen_list.append(i)

def display_room_taken_in():
    c=0
    print("List of your preferences")
    for i in self_list:
        c+=1
        print(c, " : ", i)
    c=0
    print("List of other choosing you: ")
    for i in chosen_list:
        c+=1
        print(c, " : ", i)
    

def display_All_preference():
    for i in All_preference:
        print(i)

def decide_room():
    choice = int(input("Enter the number of room to be chosen in (0 for none) "))
    if choice == 0:
        for i in chosen_list:
            All_preference.remove(i)
        return
    else:
        chosen_list[choice-1 : choice] =[]    #removes the choice
        for i in chosen_list:
            All_preference.remove(i)
        for j in self_list:
            All_preference.remove(j)



def save_allocation_to_json():
    output_data = {}
    for student_id, details in Rank_People_Dict.items():
        output_data[student_id] = {
            "rank": Id_rank_dict[student_id],
            "block": details[0],
            "room_type": details[1]
        }
    
    with open('allocation_results.json', 'w') as f:
        json.dump(output_data, f, indent=4)


choice = 0

room_taken_in()
display_room_taken_in()
decide_room()

# Run the allocation process

sort_all_preferences()
MasterFunction()
roomless_id_list()
secondary_allotment()
display()
save_allocation_to_json()

