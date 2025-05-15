from django.urls import path
from .views import add_group, list_groups


app_name = 'core'

urlpatterns = [
    path('admin/group/add/', add_group, name='add_group'),
    path('admin/group/list/', list_groups, name='list_group'),
]