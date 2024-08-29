# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from dashboard.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url="user_login")
def semester_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        department = request.POST.get('department')
        semester = request.POST.get('semester')
        email = request.POST.get('email')
        registration_date = request.POST.get('registration_date')
        print("Data request")

        # Create a new Semester entry
        Semester.objects.create(
            name=name,
            department=department,
            semester=semester,
            email=email,
            registration_date=registration_date
        )
        print("Data Stored")
        return redirect('semester_registration')

    # Fetch existing registrations for display
    queryset = Semester.objects.all()
    context = {
        'page': 'Home',
        'semester_registration': queryset
    }
    return render(request, "home.html", context)


def delete_semester(request, id):
    queryset = Semester.objects.get(id=id)
    queryset.delete()
    return redirect('semester_registration')


def update_semester(request, id):
    queryset = Semester.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        department = request.POST.get('department')
        semester_name = request.POST.get('semester')
        email = request.POST.get('email')
        registration_date = request.POST.get('registration_date')

        queryset.name = name
        queryset.department = department
        queryset.semester = semester_name
        queryset.email = email
        queryset.registration_date = registration_date
        queryset.save()

        return redirect('semester_registration')  # Adjust the redirect URL as needed

    context = {
        'semester_queryset': queryset,
    }
    return render(request, 'update_semester.html', context)


def user_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            user = User.objects.create_user(
                username=username,
                password=password
            )
            user.first_name = name
            user.save()
            messages.success(request, 'Account has been created successfully.')
            return redirect('user_registration')

    return render(request, 'user_registration.html', context={'page': 'User Registration'})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('semester_registration')  # Redirect to the homepage or another page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'user_login.html', context={'page': 'User Login'})
