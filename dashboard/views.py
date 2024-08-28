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
