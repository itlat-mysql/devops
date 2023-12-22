from uuid import uuid4

from PIL import Image
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError(_('File too large. Size should not exceed 2 MiB.'))


def get_mime_type(file):
    try:
        image = Image.open(file)
        mime_type = image.get_format_mimetype()
        return mime_type
    except Exception as e:
        return None


def allowed_content_types(value):
    allowed_types = ['image/png', 'image/jpg', 'image/jpeg', 'image/webp']
    if get_mime_type(value) not in allowed_types:
        raise ValidationError(_('Wrong image has been provided.'))


def path_and_rename(instance, filename):
    ext = filename.split('.')[-1]
    return '{}.{}'.format(uuid4().hex, ext)
