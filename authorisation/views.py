from django.shortcuts import render ,redirect

# Create your views here.

def login(request):
    return render (request,'authorisation/login.html', {})

def register(request):
    if request.method == 'POST':
        email = request.POST ['email']
        password = request.POST ['password']
        
       
        return redirect ('register')
        
    return render (request,'authorisation/register.html', {})