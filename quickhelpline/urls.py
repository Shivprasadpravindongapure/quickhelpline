# quickhelpline/urls.py
from django.contrib import admin
from django.urls import path, include
from users.views import home

urlpatterns = [
    path('', home, name='home'),  # Homepage
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),         # Users app URLs
    path('emergency/', include('emergency.urls')), # Emergency app URLs
    path('contacts/', include('contacts.urls')),   # ✅ Add this line
]
