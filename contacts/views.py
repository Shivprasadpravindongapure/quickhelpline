# contacts/views.py
from django.shortcuts import render
from django.http import HttpResponse

def contact_list(request):
    return render(request, 'contacts/contact_list.html')

def helpline_list(request):
    return render(request, 'contacts/helpline_list.html')

def location_view(request):
    return render(request, 'contacts/location.html')

def sos_alert(request):
    return HttpResponse("🚨 SOS Alert Sent! (Feature coming soon)")
