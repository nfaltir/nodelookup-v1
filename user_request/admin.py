from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import UserRequest

from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm

client_desc = "Client research request form data"
admin_desc = "Staff request submissions"

class UserRequestAdmin(ModelAdmin, ImportExportModelAdmin):

    
    fieldsets = (
        ('Client',{
            'fields':('user', 'channel_name', 'channel_industry','channel_link', 'channel_id','specific_questions'),
            'description': '%s' % client_desc,
        }),
        ('Admin', {
            'fields':('status', 'report_file', 'completed_at',),
            'description': '%s' % admin_desc,
        })
    )
    list_display = ('user', 'channel_name', 'channel_industry', 'status','channel_id', 'created_at')
    list_filter = ('status', 'channel_industry')
    search_fields = ('channel_name', 'channel_id')

    import_form_class = ImportForm
    export_form_class = ExportForm


    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_staff:
            return ['status']
        return []

    # Limit report_file field visibility to admins only
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if not request.user.is_staff:
            # Remove the 'report_file' field from non-admin users
            fields.remove('report_file')
        return fields

admin.site.register(UserRequest, UserRequestAdmin)
