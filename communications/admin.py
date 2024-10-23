from django.contrib import admin
from .models import Message
from unfold.admin import ModelAdmin

class MessageAdmin(ModelAdmin):
    list_display = ('sender', 'subject', 'status', 'is_read', 'timestamp')
    list_filter = ('status', 'is_read')
    search_fields = ('sender__username', 'subject')

admin.site.register(Message, MessageAdmin)
