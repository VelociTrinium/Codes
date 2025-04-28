import json

# Load data from JSON files
with open('students.json', 'r') as f:
    students_data = json.load(f)

with open('rooms.json', 'r') as f:
    rooms_data = json.load(f)

with open('preferences.json', 'r') as f:
    preferences_data = json.load(f)

# Initialize data structures
LoginIds = list(students_data.keys())
Id_rank_dict = {student_id: details['rank'] for student_id, details in students_data.items()}
Rank_People_Dict = {student_id: [details['block'], details['room_type']] for student_id, details in students_data.items()}
Block_list = list(rooms_data.keys())

# Initialize room availability
Block_Room_Types = {}
for block, room_types in rooms_data.items():
    Block_Room_Types[block] = {}
    for room_type, details in room_types.items():
        Block_Room_Types[block][room_type] = details['rooms']

left_people_list = []
All_preference = []

# Process preferences from JSON
for pref in preferences_data:
    student_id = pref['id']
    for preference in pref['preferences']:
        pref_no = preference['preference_no']
        block = preference['block']
        room_type = preference['room_type']
        roommates = preference['roommates']
        All_preference.append([student_id, pref_no, block, room_type, roommates])

def is_room_available(block, room_type):
    if Block_Room_Types.get(block, {}).get(room_type, 0) > 0:
        return True
    return False

def is_Id_allocated(student_id):
    if Rank_People_Dict[student_id][0] == "":
        return False
    return True

def sort_all_preferences():
    All_preference.sort(key=lambda x: Id_rank_dict.get(x[0], x[1]), reverse=False)

def MasterFunction():
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
        all_roommates_have_same_pref = True
        for roommate in preference[4]:
            roommate_has_pref = False
            for pref in All_preference:
                if pref[0] == roommate and pref[2] == block and pref[3] == room_type and set(pref[4]) == set(preference[4]):
                    roommate_has_pref = True
                    break
            if not roommate_has_pref:
                all_roommates_have_same_pref = False
                break

        if not all_roommates_have_same_pref:
            continue

        # Allocate the room
        for student in preference[4]:
            Rank_People_Dict[student][0] = block
            Rank_People_Dict[student][1] = room_type
        Block_Room_Types[block][room_type] -= 1

def roomless_id_list():
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

# Run the allocation process
sort_all_preferences()
MasterFunction()
roomless_id_list()
secondary_allotment()
display()
save_allocation_to_json()

