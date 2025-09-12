from django.urls import path
from . import views

urlpatterns = [
    path('courses/<int:pk>/enroll/', views.enroll_course, name='enroll_course'),
]
