from django.urls import path
from django.views.generic import TemplateView

from contact_form.views import ContactFormView

from marble.cms.forms import TwoRockContactForm


app_name = "website"

# URLs for claim views
urlpatterns = [
    # path('', TemplateView.as_view(template_name='cms/homepage.html'), name="homepage"),
    path('careers/', TemplateView.as_view(template_name='cms/careers.html'), name="careers"),
    path('contact/', ContactFormView.as_view(form_class=TwoRockContactForm), name='contact_form'),
]
