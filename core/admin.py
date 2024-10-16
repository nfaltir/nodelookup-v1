from django.contrib import admin
from .models import GalleryReport

@admin.register(GalleryReport)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('channel', 'industry', 'created_at')  # Display key fields
    readonly_fields = ('created_at',)  # Make sure 'created_at' is read-only in admin
