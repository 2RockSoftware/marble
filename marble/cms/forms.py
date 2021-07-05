from django import forms
from django.conf import settings
from django.core.mail import EmailMessage

from contact_form.forms import ContactForm


class TwoRockContactForm(ContactForm):
    organization = forms.CharField()
    phone_number = forms.CharField()
    budget = forms.CharField()

    def send(self):
        # FIXME: What do we need name for?
        name = self.cleaned_data["name"]
        org = self.cleaned_data["organization"]
        phone_number = self.cleaned_data["phone_number"]
        budget = self.cleaned_data["budget"]
        email = self.cleaned_data["email"]
        message = self.cleaned_data["body"]
        email_body = """
            Name: {name} \n
            Email: {email} \n
            Org: {org} \n
            Phone Number: {phone_number} \n
            Budget: {budget} \n\n
            Message: {message} \n
        """.format(message=message, name=name, email=email, org=org, phone_number=phone_number, budget=budget)
        emails = (
            [settings.CONTACT_EMAIL]
            if not settings.DEBUG
            else [
                settings.TEST_EMAIL,
            ]
        )
        headers = {'Reply-To': email}
        msg = EmailMessage("You got mail!", email_body, settings.CONTACT_EMAIL, emails, headers=headers)
        msg.send()
