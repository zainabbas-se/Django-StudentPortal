# views.py
from django.shortcuts import render, redirect
from dashboard.models import Semester


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
