from django.db import models

class AccessEntry(models.Model):
    uid = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    access_start = models.DateTimeField()
    access_duration = models.DurationField()  # Example: 2 hours
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uid} ({self.email or self.phone or 'No contact'})"
