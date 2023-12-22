from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext as _

from .forms import ContactsForm
from .models import Message
from .utils import get_client_ip, get_ip_msg_qty_within_minutes


def form(request):
    if request.method == "POST":
        contacts_form = ContactsForm(request.POST)
        if contacts_form.is_valid():
            ip = get_client_ip(request)
            if get_ip_msg_qty_within_minutes(ip, 3) == 0:
                Message(email=contacts_form.cleaned_data['email'], content=contacts_form.cleaned_data['content'], ip=ip,
                        verified=False).save()

                messages.success(request, _('Your question has been submitted successfully.'))
                return redirect(reverse('contacts:form'))
            else:
                messages.error(request, _('You are allowed to ask question only 1 time per 3 minutes.'))
    else:
        contacts_form = ContactsForm()

    return render(request, 'contacts/form.html', {'contacts_form': contacts_form})
