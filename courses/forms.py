from django import forms
from .models import CourseList, Course, Module, Video, Topic


class CourseListForm(forms.ModelForm):
    class Meta:
        model = CourseList
        fields = ['title', 'description']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['courselist', 'title', 'description', 'author']


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['course', 'title', 'description']

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['module', 'title', 'description']



class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['module', 'title', 'video_file', 'duration']
