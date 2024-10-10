from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    # Subject choices
    SUBJECT_CHOICES = [
        ('general_inquiry', 'General Inquiry'),
        ('product_ideas', 'Product Ideas'),
        ('technical_support', 'Technical Support'),
        ('reports', 'Reports'),
    ]
    
    # Message status choices
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]

    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    admin_reply = models.TextField(null=True, blank=True)  # Admin's reply field
    admin_reply_file = models.FileField(upload_to='admin_replies/', null=True, blank=True)  # Optional file upload
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')  # Status field

    def __str__(self):
        return f"From {self.sender.username} - {self.subject} - {self.get_status_display()}"
