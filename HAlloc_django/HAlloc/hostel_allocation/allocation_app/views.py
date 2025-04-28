import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt
import random

# Load data from JSON files
def load_json(filename):
    file_path = os.path.join(settings.BASE_DIR, "allocation_app", "data", filename)
    if not os.path.exists(file_path):
        return {}  # Return an empty dictionary if file not found to avoid errors
    with open(file_path, "r") as file:
        return json.load(file)

students_data = load_json('students.json')
rooms_data = load_json('rooms.json')
preferences_data = load_json('preferences.json')

# Initialize data structures
Id_rank_dict = {student_id: details['rank'] for student_id, details in students_data.items()}
Rank_People_Dict = {student_id: [details['block'], details['room_type']] for student_id, details in students_data.items()}

# Login view
def login_view(request):
    if request.method == "POST":
        regNumber = request.POST.get("registerNumber").strip()
        password = request.POST.get("password").strip()

        # Validate student ID and password
        if regNumber in students_data:
            if regNumber == password:  # Match student ID with password
                # Store register number in session
                request.session['userReg'] = regNumber
                return redirect("dashboard")  # Redirect to the dashboard
            else:
                # Incorrect password
                return render(request, "login.html", {"error": "Incorrect password! Password should match Register Number."})
        else:
            # Student ID not found
            return render(request, "login.html", {"error": "Invalid Register Number. Please check your ID."})

    return render(request, "login.html")

# Dashboard view
def dashboard_view(request):
    return render(request, 'dashboard.html')

def room_selection_view(request):
    reg_number = request.session.get('userReg')
    if not reg_number:
        return redirect('login')
    return render(request, 'room_selection.html',{'reg_number': reg_number,})

# Rank view


def rank_view(request):
    # Check if user is logged in by checking session for the 'userReg' value
    reg_number = request.session.get('userReg')
    if not reg_number:
        return redirect('login')  # Redirect to login page if user is not logged in

    print("User Registration Number from session:", reg_number)  

    # Load student data from JSON file
    # json_path = os.path.join(os.path.dirname(__file__), 'students.json')
    json_path = os.path.join(settings.BASE_DIR, "allocation_app", "data", "students.json")
    try:
        with open(json_path, 'r') as file:
            student_data = json.load(file)
        print("Loaded Student Data:", student_data)  
    except (FileNotFoundError, json.JSONDecodeError):
        student_data = {}

    # Print available registration numbers in JSON
    print("Available Registration Numbers:", student_data.keys())  

    # Get user rank based on registration number
    user_rank = student_data.get(reg_number, {}).get("rank", "N/A")

    return render(request, 'rank.html', {'reg_number': reg_number, 'user_rank': user_rank})

# def rank_view(request):
#     # Check if user is logged in by checking session for the 'userReg' value
#     reg_number = request.session.get('userReg')
#     if not reg_number:
#         return redirect('login')  # Redirect to login page if user is not logged in
    
#     # Generate a random rank for the user
#     user_rank = random.randint(1, 500)  # Simulating rank generation
#     return render(request, 'rank.html', {'reg_number': reg_number, 'user_rank': user_rank})


# def rank_view(request):
#     students_data = load_json("students.json")  # Load JSON file

#     return render(request, "rank.html", {"students": students_data.items()})

# Preferences view
def get_students_json(request):
    file_path = os.path.join(settings.BASE_DIR, "allocation_app", "data", "students.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "File not found"}, status=404)

@csrf_exempt   
def save_preference(request):
    reg_number = request.session.get('userReg')
    if not reg_number:
        return redirect('login')
    
    if request.method == 'POST':
        try:
            # Read the data from the request body
            data = json.loads(request.body)
            student_id = data.get('id')
            preference_no = data.get('preference_no')
            block = data.get('block')
            room_type = data.get('room_type')
            roommates = data.get('roommates')

            # You can save the data to your preferences file or database
            preferences_file_path = os.path.join(settings.BASE_DIR, 'allocation_app', 'data', 'preferences.json')
            if os.path.exists(preferences_file_path):
                with open(preferences_file_path, 'r') as file:
                    preferences_data = json.load(file)
            else:
                preferences_data = []

            preferences_data.append({
                'id': student_id,
                'preference_no': preference_no,
                'block': block,
                'room_type': room_type,
                'roommates': roommates,
            })

            # Save updated preferences to JSON
            with open(preferences_file_path, 'w') as file:
                json.dump(preferences_data, file, indent=4)

            return JsonResponse({"status": "success", "message": "Preference saved successfully!"}, status=200)

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)    

def preferences_view(request):
    reg_number = request.session.get('userReg')
    if not reg_number:
        return redirect('login')
    if request.method == 'POST':
        student_id = request.POST['student_id']
        block = request.POST.get('block')
        room_type = request.POST.get('room_type')
        roommates = request.POST.getlist('roommates')

        # Prepare the preference data
        preference_data = {
            'id': student_id,
            'preference_no': len(preferences_data) + 1,  # Increment preference number
            'block': block,
            'room_type': room_type,
            'roommates': roommates
        }

        # Append the new preference to the preferences list
        preferences_data.append(preference_data)

        # Save preferences to the JSON file
        preferences_file_path = os.path.join(settings.BASE_DIR, 'allocation_app', 'data', 'preferences.json')
        with open(preferences_file_path, 'w') as file:
            json.dump(preferences_data, file, indent=4)

        return redirect('dashboard')  # Redirect to dashboard after successful preference submission

    student_ids = list(students_data.keys())  # Get list of student IDs
    return render(request, 'preferences.html', {'students': student_ids,'reg_number': reg_number})

