from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext as _

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    search_fields = ('title', 'content', 'active')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 100px;" />')
        else:
            return _('No Image')

    image_preview.short_description = _('Image Preview')


admin.site.register(Post, PostAdmin)
