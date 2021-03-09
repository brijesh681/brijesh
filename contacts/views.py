from django.shortcuts import render,redirect
from contacts.models import contact

# Create your views here.
def con1(request):
    if request.method=="POST":
        print("this is post")
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        br = contact(name=name, email=email, subject=subject, message=message)
        br.save()
        print('sucessfully submit')
        return redirect('/')
    else:
        return render(request,'contact/con1.html')
        
        