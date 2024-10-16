from django.db import models

class GalleryReport(models.Model):
    channel = models.CharField(max_length=255)
    channel_link = models.URLField(default='http://youtube.com') 
    industry = models.CharField(max_length=255)
    channel_description = models.TextField()
    pdf_file = models.FileField(upload_to='gallery/pdfs/')  # PDF upload field
    created_at = models.DateField(auto_now_add=True)  # Automatically sets the date when the report is created
    channel_image = models.ImageField(upload_to='gallery/images/', blank=True, null=True)  # Optional image upload

    def __str__(self):
        return f"{self.channel} - {self.industry}"

