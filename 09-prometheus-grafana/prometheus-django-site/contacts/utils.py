from django.utils import timezone

from contacts.models import Message


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', '')
    return ip


def get_ip_msg_qty_within_minutes(ip, minutes):
    minutes_ago = timezone.now() - timezone.timedelta(minutes=minutes)
    return Message.objects.filter(created_at__range=[minutes_ago, timezone.now()], ip=ip).count()
