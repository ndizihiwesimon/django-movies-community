from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

def register(request):
    if request.method == 'POST':
        first_name = request.POST['Firstname']
        last_name = request.POST['Lastname']
        email = request.POST['Email']
        photo = request.FILES['Photo']
        gender = request.POST['Gender']
        birthdate = request.POST['Dob']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                print('Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(email=email, password=password1,
                                                first_name=first_name, last_name=last_name, photo=photo, gender=gender,
                                                birthdate=birthdate)
                user.save()
                print('User created successfully')
                return redirect('login')
        else:
            print('Password not matching')
        return redirect('/')
    else:
        return render(request, "auth/register.html")


def login(request):
    if request.method == 'POST':
        email = request.POST['Email']
        password = request.POST['Password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            print('Logged in successful')
            return redirect('dashboard')
        else:
            print('Invalid credentials')
            return redirect('login')

    else:
        return render(request, "auth/login.html")
