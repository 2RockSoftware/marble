from django.conf import settings

from contact_form.forms import ContactForm
from captcha.fields import ReCaptchaField, ReCaptchaV3


class TwoRockContactForm(ContactForm):
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                'required_score': settings.RECAPTCHA_REQUIRED_SCORE
            }
        )
    )
