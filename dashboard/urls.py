from django.urls import path
from .views import teacher_index, teacher_info


app_name = 'dashboard'

urlpatterns = [
    path('teacher/info', teacher_info, name='teacher_info'),
    path('teacher/', teacher_index, name='teacher_index'),
]