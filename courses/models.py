from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta


class CourseList(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    courselist = models.ForeignKey(CourseList, related_name="courses", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # faqat teacher bo‘lishi uchun formda filter qilamiz
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    profile_image = models.ImageField(upload_to='course_images/', blank=True, null=True)

    # qo‘shimchalar
    modules_count = models.PositiveIntegerField(default=0)  # admindan qo‘shish mumkin
    rating = models.FloatField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    total_videos = models.PositiveIntegerField(default=0)
    min_duration = models.DurationField(default=timedelta, blank=True, null=True)
    students_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def update_counts(self):
        """Module va video sonini yangilash"""
        self.modules_count = self.modules.count()
        self.total_videos = Video.objects.filter(module__course=self).count()
        self.students_count = self.enrollments.count()
        # min_duration hisoblash (eng qisqa video)
        min_video = Video.objects.filter(module__course=self).order_by("duration").first()
        self.min_duration = min_video.duration if min_video else None
        self.save()


class Module(models.Model):
    course = models.ForeignKey(Course, related_name="modules", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.course.title} → {self.title}"


class Topic(models.Model):
    module = models.ForeignKey(Module, related_name="topics", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.module.title} → {self.title}"


class Video(models.Model):
    module = models.ForeignKey(Module, related_name="videos", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to="videos/")
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"{self.module.title} → {self.title}"


class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="enrollments", on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    # progress qo‘shamiz: necha foizini tugatgan
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user} -> {self.course} ({self.progress}%)"
