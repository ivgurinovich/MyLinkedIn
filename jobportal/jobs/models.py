from django.db import models
from django.conf import settings


class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('remote', 'Remote'),
    ]

    title = models.CharField(max_length=255)
    company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, default='Remote')
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='full_time')
    is_active = models.BooleanField(default=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-posted_at']
