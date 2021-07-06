from django.contrib import admin

from marble.cms.models import ContactFormSubmission


class ContactFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "organization")


admin.site.register(ContactFormSubmission, ContactFormSubmissionAdmin)
