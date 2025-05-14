from django.urls import path

from .views import register, get_profile_form


app_name = 'users'
urlpatterns = [
    path('register/', register, name='register'),
    path('get-profile-form/', get_profile_form, name='get_profile_form'),
]