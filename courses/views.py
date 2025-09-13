from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment, Module, Topic, Video
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

@login_required
def continue_learning(request, pk):
    course = get_object_or_404(Course, pk=pk)
    modules = course.modules.all()

    # Foydalanuvchi enroll bo'lgan kursini tekshiramiz
    enrollment = Enrollment.objects.filter(user=request.user, course=course).first()

    return render(request, "module_detail.html", {
        "course": course,
        "modules": modules,
        "enrollment": enrollment
    })



@login_required
def topic_list(request, pk, module_id=None):
    course = get_object_or_404(Course, pk=pk)
    
    # Get modules for the filter
    modules = course.modules.all()
    
    # Get topics - filter by module if specified
    if module_id:
        active_module = get_object_or_404(Module, pk=module_id, course=course)
        topics = Topic.objects.filter(module=active_module)
    else:
        active_module = None
        topics = Topic.objects.filter(module__course=course)

    # Check if user is enrolled
    enrollment = Enrollment.objects.filter(user=request.user, course=course).first()

    return render(request, "topic_list.html", {
        "course": course,
        "topics": topics,
        "modules": modules,
        "active_module": active_module,
        "enrollment": enrollment
    })



@login_required
def topic_detail(request, pk, topic_id):
    course = get_object_or_404(Course, pk=pk)
    topic = get_object_or_404(Topic, pk=topic_id, module__course=course)
    
    # Faqat ushbu mavzuga tegishli videolarni olish
    videos = Video.objects.filter(topic=topic)
    
    # Check enrollment
    enrollment = Enrollment.objects.filter(user=request.user, course=course).first()
    if not enrollment:
        messages.error(request, "Siz ushbu kursga yozilmagansiz.")
        return redirect('enroll_course', pk=course.pk)

    return render(request, "video.html", {
        "course": course,
        "topic": topic,
        "videos": videos,
        "enrollment": enrollment
    })