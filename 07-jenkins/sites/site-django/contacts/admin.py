from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'ip', 'verified',)
    search_fields = ('email', 'ip', 'content',)
    readonly_fields = ('ip',)

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Message, MessageAdmin)
