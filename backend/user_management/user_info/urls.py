from django.urls import path 
from . import views

urlpatterns = [
    path('roles/',views.get_roles),
    path('users/',views.get_users),
    path('users/create/',views.create_user)
]
