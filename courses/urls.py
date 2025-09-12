from django.urls import path
from . import views

urlpatterns = [
    path('courses/<int:pk>/enroll/', views.enroll_course, name='enroll_course'),
    path('courses/<int:pk>/continue/', views.continue_learning, name='continue_learning'),
    path('courses/<int:pk>/topics/', views.topic_list, name='topic_list'),  # endi Course.pk bo‘yicha
]
