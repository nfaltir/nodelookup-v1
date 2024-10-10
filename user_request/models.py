from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserRequest(models.Model):
    INDUSTRY_CHOICES = [
        ('Gaming', 'Gaming'),
        ('Lifestyle', 'Lifestyle'),
        ('Fitness', 'Fitness'),
        ('Education', 'Education'),
        ('Technology', 'Technology'),
        # Add more industry options as needed
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel_name = models.CharField(max_length=255)
    channel_link = models.URLField()
    channel_id = models.CharField(max_length=100)
    channel_industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)
    specific_questions = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    # New field for admin to upload a PDF report
    report_file = models.FileField(upload_to='reports/', blank=True, null=True, help_text="Upload the report in PDF format (admin only).")
    # New field for the timestamp when the status is updated to Completed
    completed_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Automatically set completed_at if status is updated to 'Completed'
        if self.status == 'Completed' and not self.completed_at:
            self.completed_at = timezone.now()
        elif self.status != 'Completed':
            self.completed_at = None  # Reset if status is changed to anything else
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s Request - {self.channel_name}"

    @property
    def status_class(self):
        if self.status == "Pending":
            return "text-amber-500"  # Tailwind CSS class for yellow
        elif self.status == "In Progress":
            return "text-blue-500"  # Tailwind CSS class for blue
        elif self.status == "Completed":
            return "text-emerald-400"  # Tailwind CSS class for green
        elif self.status == "Rejected":
            return "text-red-500"  # Tailwind CSS class for red
        return "text-gray-500"  # Default class if no status matches
