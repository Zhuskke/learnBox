from django.db import models
from django.conf import settings
from accounts.models import User
from django.utils import timezone

# Create your models here.
class AssignmentSubmission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.university_id

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    marks = models.CharField(max_length=20)
    duration = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title

