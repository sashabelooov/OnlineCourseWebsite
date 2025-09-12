from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, ProfileUpdateForm, EmailAuthenticationForm
from django.contrib.auth.decorators import login_required
from courses.models import Course, Enrollment



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)  # faqat POST malumotlari
        if form.is_valid():
            user = form.save(commit=False)   # userni yaratamiz lekin saqlamaymiz
            user.username = user.email       # emailni username qilib qo'yamiz
            user.save()                      # DB ga saqlaymiz
            login(request, user)             # avtomatik login
            return redirect('login')          # asosiy sahifa
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})






def login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = EmailAuthenticationForm()
    return render(request, 'login.html', {'form': form})




@login_required
def profile_update_view(request):
    if request.user.is_superuser:
        return redirect('profile')

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'profile_update.html', {'form': form})


@login_required
def profile_view(request):
    enrollments = Enrollment.objects.filter(user=request.user).select_related("course")
    enrolled_courses = [en.course for en in enrollments]
    
    # Get all courses that the user is not enrolled in
    enrolled_course_ids = [ec.id for ec in enrolled_courses]
    courses = Course.objects.all()
    print(f"courses:{courses}")
    return render(request, 'profile.html', {
        'enrolled_courses': enrolled_courses,
        'courses': courses,
    })


def logout_view(request):
    logout(request)
    return redirect('landing')

