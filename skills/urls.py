from django.urls import path
from .import views

urlpatterns = [
    path('n/',views.skills,name='skills'),
]
