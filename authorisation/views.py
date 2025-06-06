from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from django.contrib.auth import authenticate, login as auth_login



from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
 







def anonymous_required(function=None, redirect_url=None):

   if not redirect_url:
       redirect_url = 'dashboard'

   actual_decorator = user_passes_test(
       lambda u: u.is_anonymous,
       login_url=redirect_url
   )

   if function:
       return actual_decorator(function)
   return actual_decorator



@anonymous_required
def login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        email = request.POST ['email'].replace('','' ).lower()
        password = request.POST['password']
        user = auth.authenticate( username = email, password = password)
        if user:
            auth.login(request, user)
                
            return redirect('home')
        else:
            messages.error(request, 'account does not exit plz sign in')
            return redirect('register')
    return render (request,'authorisation/login.html', {})

# def login(request):
    

 
#      email = request.POST ['email'].replace('','' ).lower()
#      password = request.POST['password']
#      user = auth.authenticate( username = email, password = password)
#      if user is not None:
#         authlogin(request, user)
#         return redirect('dashboard')
#      else:
#             messages.error(request, 'account does not exit plz sign in')
#             return redirect('register')
#      return render (request,'authorisation/login.html', {})

@anonymous_required
def register(request):
    if request.method =='POST':
        
        email = request.POST ['email'].replace('','' ).lower()
        password1 = request.POST ['password1']
        password2 = request.POST ['password2']
        
      
    
     
        if not password1 == password2:
            
            messages.error(request, 'Password do not match')
            return redirect('register')
             
        if User.objects.filter(email=email).exists():
            messages.error(request, "A USer with the email address ; {} already exists, please use a different email". format(email))
            return redirect('register')
            
        user = User.objects.create_user(email=email,username=email,password=password2)
        user.save()
        auth.login(request,user)
        return redirect ('dashboard')
                
      
    return render (request,'authorisation/register.html',{} )
    
   #using the long-required decorator
@login_required
def logout(request):
  auth.logout(request)
  return redirect('login')


