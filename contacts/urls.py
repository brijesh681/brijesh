from django.urls import path
from .import views

urlpatterns = [
    path('p/',views.con1,name='contacts')
]
