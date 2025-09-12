from django.contrib import admin
from .models import CourseList, Course, Module, Video, Topic


@admin.register(CourseList)
class CourseListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'courselist', 'author')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'module')
    search_fields = ('title',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'module')
