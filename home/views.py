from django.contrib.auth import password_validation
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from user_module.models import profile_model
from home.forms import feedback_form
from django.contrib.auth.decorators import login_required

def home(request):
    user_log = request.user
    if user_log.is_authenticated:
        return redirect('user_module/skills')
    else:  
        return render(request, 'home.html')

def login(request):
    user_log = request.user
    if user_log.is_authenticated:
        return redirect('user_module/skills')
    else:
        if 'submit' in request.POST:
            if 'login' == request.POST.get('submit'):
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(request, username=username, password=password)
                if user is None:
                    context = {'error': 'Wrong credentials'}
                    return render(request,'login_error.html',context)
                else:
                    auth.login(request,user)
                    return redirect('user_module/skills')
            elif 'signup' == request.POST.get('submit'):
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                confirm_password = request.POST['confirm_password']
                check_password = validate_password(password, user=None, password_validators=None)
                if check_password == None:
                    if password==confirm_password:
                        if User.objects.filter(username=username).exists():
                            context = {'error': 'Username already exists!!!'}
                            return render(request,'login_error.html',context)
                        elif User.objects.filter(email=email).exists():
                            context = {'error': 'Email already exists!!!'}
                            return render(request,'login_error.html',context)
                        else:
                            user = User.objects.create_user(username=username, email=email, password=password)
                            profile = profile_model.objects.create(user=username, email=email)
                            user.save()
                            profile.save()
                            context = {'success':'Sign up successfull !!!'}
                            return render(request, 'login.html', context)                          
                    else:
                        context = {'error': 'Password not matching!!!'}
                        return render(request,'login_error.html',context)
                else:   
                    context = {'password_error': check_password}
                    return render(request,'login_error.html',context)
        return render(request, 'login.html')

def feedback(request):
    form = feedback_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
        else:
            form = feedback_form(request.POST or None)
            context = {'form':form, 'message':"Unable to take your feedback"}
            return render(request, 'feedback.html', context)            
    context = {'form' : form}
    return render(request, 'feedback.html', context)

def errorlogin(request):
    context = {'error': 'Wrong credentials'}
    return render(request,'login_error.html',context)
    