from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment
from django.contrib import messages

@login_required
def enroll_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    enrollment = Enrollment.objects.filter(user=request.user, course=course).first()
    is_enrolled = enrollment is not None
    
    if request.method == "POST":
        action = request.POST.get('action')
        
        if action == 'enroll' and not is_enrolled:
            Enrollment.objects.get_or_create(user=request.user, course=course)
            messages.success(request, f"You have successfully enrolled in {course.title}")
            return redirect('profile')  # Remove the pk parameter
            
        elif action == 'unenroll' and is_enrolled:
            enrollment.delete()
            messages.success(request, f"You have been unenrolled from {course.title}")
            return redirect('profile')
        
    return render(request, "enroll_course.html", {
        "course": course,
        "is_enrolled": is_enrolled
    })