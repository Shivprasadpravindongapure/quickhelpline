# contacts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('helplines/', views.helpline_list, name='helpline_list'),
    path('location/', views.location_view, name='location_view'),
    path('sos/', views.sos_alert, name='sos_alert'),
]
