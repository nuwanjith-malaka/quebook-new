from django.urls import path
from .views import  AskerView, EditProfileView
urlpatterns = [
    path('editprofile/<int:pk>/', EditProfileView.as_view(), name='edit_profile'),
    path('askers/<int:pk>/', AskerView, name='asker'),
]