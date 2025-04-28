import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import os




PREFERENCES_FILE = os.path.join("data", "preferences.json")

@csrf_exempt
def save_preference(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_id = data.get("id")
            new_preference = {
                "preference_no": data.get("preference_no"),
                "block": data.get("block"),
                "room_type": data.get("room_type"),
                "roommates": data.get("roommates", [])
            }

            try:
                with open(PREFERENCES_FILE, "r") as f:
                    preferences = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                preferences = []

            user_entry = next((p for p in preferences if p["id"] == user_id), None)
            if user_entry:
                new_preference["preference_no"] = len(user_entry["preferences"]) + 1
                user_entry["preferences"].append(new_preference)
            else:
                preferences.append({"id": user_id, "preferences": [new_preference]})

            with open(PREFERENCES_FILE, "w") as f:
                json.dump(preferences, f, indent=4)

            return JsonResponse({"success": True, "message": "Preference added successfully."})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "message": "Invalid request method."})

def preference_form(request):
    return render(request, "preferences.html")
