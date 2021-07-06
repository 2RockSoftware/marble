from django import forms
from django.conf import settings
from django.core.mail import EmailMessage

from marble.cms.models import ContactFormSubmission


class TwoRockContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    organization = forms.CharField()
    phone_number = forms.CharField()
    budget = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ContactFormSubmission
        fields = "__all__"

    def save(self, commit=True):
        instance = super(TwoRockContactForm, self).save(commit=True)
        self.send()
        return instance

    def send(self):
        name = self.cleaned_data["name"]
        org = self.cleaned_data["organization"]
        phone_number = self.cleaned_data["phone_number"]
        budget = self.cleaned_data["budget"]
        email = self.cleaned_data["email"]
        message = self.cleaned_data["message"]
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
