from django.urls import path
from .import views

urlpatterns = [
    path('b/',views.serv1,name='service'),

]
