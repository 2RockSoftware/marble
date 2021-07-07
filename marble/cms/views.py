import json
import logging
import requests

from django.conf import settings
from django.http import HttpResponse

from marble.cms.forms import TwoRockContactForm

logger = logging.getLogger(__name__)


def contact(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = TwoRockContactForm(data)
        if form.is_valid():
            # save data into database even if recaptcha fails
            form.save()
            # recaptcha validation
            recaptcha_response = data.get('g_recaptcha_response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            validation_response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = validation_response.json()
            if result['success']:
                form.send()  # only send email if submission passes recaptcha challenge
                data = {
                    "message": "Your inquiry has been successfully submitted. We will contact you as soon as possible.",
                    "errors": False
                }
                return HttpResponse(status=200, content=json.dumps(data))
            else:
                data = {
                    "message": "Sorry but your submission didn't made it through our spam filter. Please give us a "
                               "call at (919) 636-0953.",
                    "errors": True
                }
                return HttpResponse(status=200, content=json.dumps(data))
        else:
            data = {
                "message": [error for error in form.errors],
                "errors": False
            }
            return HttpResponse(status=200, content=json.dumps(data))

    return HttpResponse(status=200, content=json.dumps({"message": "Only POST requests are supported.", "errors": True}))
