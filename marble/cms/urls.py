from django.urls import path
from django.views.generic import TemplateView

from marble.cms.views import contact

app_name = "website"

# URLs for claim views
urlpatterns = [
    # path('', TemplateView.as_view(template_name='cms/homepage.html'), name="homepage"),
    path('careers/', TemplateView.as_view(template_name='cms/careers.html'), name="careers"),
    path('contact-submit/', contact, name='contact_form_submit'),
]
