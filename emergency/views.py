from django.shortcuts import render
from django.http import JsonResponse
import requests

# 🚨 List of emergency helplines
def helpline_list(request):
    helplines = [
        {"name": "Police", "number": "100"},
        {"name": "Ambulance", "number": "108"},
        {"name": "Fire", "number": "101"},
        {"name": "Women Helpline", "number": "1091"},
        {"name": "Child Helpline", "number": "1098"},
    ]
    return render(request, "emergency/helpline_list.html", {"helplines": helplines})


# 📍 Real-time location (uses IP API)
def location_view(request):
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
    except:
        data = {"error": "Could not fetch location"}
    return render(request, "emergency/location.html", {"location": data})


# 🔴 SOS (dummy simulation)
def sos_alert(request):
    return render(request, "emergency/sos.html", {"message": "SOS Alert Sent Successfully!"})
