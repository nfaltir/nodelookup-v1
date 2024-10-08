from django.contrib import admin
from .models import UserRequest

class UserRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'channel_name', 'status', 'created_at')
    list_filter = ('status', 'channel_industry')
    search_fields = ('channel_name', 'channel_id')

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_staff:
            return ['status']
        return []

admin.site.register(UserRequest, UserRequestAdmin)
