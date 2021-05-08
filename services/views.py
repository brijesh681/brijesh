from django.shortcuts import render

# Create your views here.
def serv1(request):
    return render(request,'service/serv1.html')
