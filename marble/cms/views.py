import logging
import requests

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import reverse, render

from marble.cms.forms import TwoRockContactForm

logger = logging.getLogger(__name__)


def contact(request):
    success_url = reverse("contact_form_sent")
    if request.method == "POST":
        form = TwoRockContactForm(request=request.POST, data=request.POST)
        if form.is_valid():
            # recaptcha validation
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            validation_response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = validation_response.json()
            if result['success']:
                form.send()
                return HttpResponseRedirect(success_url)
    else:
        form = TwoRockContactForm()

    context = {
        "form": form,
        "page": {
            "title": "Contact Us"
        },
        "GOOGLE_RECAPTCHA_SITE_KEY": settings.GOOGLE_RECAPTCHA_SITE_KEY,
    }
    return render(request, "cms/contact_page.html", context)
