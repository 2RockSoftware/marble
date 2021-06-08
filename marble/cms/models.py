from django.db import models

from django.utils.translation import gettext as _

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from marble.cms.blocks import FounderBlock, DeveloperBlock, ProjectBlock, ClientsLogos
from marble.cms.forms import TwoRockContactForm


class HomePage(Page):
    elevator_pitch = models.TextField(blank=True)
    what_we_build_section = StreamField(
        [
            ("heading", blocks.CharBlock(classname="full")),
            ("subheading", blocks.CharBlock(classname="full")),
            ("html", blocks.RawHTMLBlock(icon="code", label="Raw HTML")),
        ],
        blank=True,
        null=True,
    )
    how_we_work_section = StreamField(
        [
            ("heading", blocks.CharBlock(classname="full")),
            ("subheading", blocks.CharBlock(classname="full")),
            ("html", blocks.RawHTMLBlock(icon="code", label="Raw HTML")),
        ],
        blank=True,
        null=True,
    )

    about_us_section = StreamField(
        [
            ("heading", blocks.CharBlock(classname="full")),
            ("subheading", blocks.CharBlock(classname="full")),
            ("description", blocks.RawHTMLBlock(icon="code", label="Raw HTML")),
            ("founder", FounderBlock(classname="full")),
            ("developer", DeveloperBlock(classname="full")),
        ],
        blank=True,
        null=True,
    )

    clients_section = StreamField(
        [
            ("heading", blocks.CharBlock(classname="full")),
            ("subheading", blocks.CharBlock(classname="full")),
            ("logos", ClientsLogos(classname="full")),
            ("html", blocks.RawHTMLBlock(icon="code", label="Raw HTML")),
            ("image", ImageChooserBlock("image")),
        ],
        blank=True,
        null=True,
    )

    the_quarry_section = StreamField(
        [
            ("heading", blocks.CharBlock(classname="full")),
            ("subheading", blocks.CharBlock(classname="full")),
            ("html", blocks.RawHTMLBlock(icon="code", label="Raw HTML")),
            ("project", ProjectBlock()),
        ],
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('elevator_pitch', classname="full"),
        StreamFieldPanel('what_we_build_section', classname="full"),
        StreamFieldPanel('how_we_work_section', classname="full"),
        StreamFieldPanel('about_us_section', classname="full"),
        StreamFieldPanel('clients_section', classname="full"),
        StreamFieldPanel('the_quarry_section', classname="full"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request)
        from puput.models import BlogPage

        blog = BlogPage.objects.first()
        blog_entries = blog.get_entries()
        context.update({
            "blog": blog,
            "blog_entries": blog_entries,
            "contact_form": TwoRockContactForm(request=request),
        })
        return context


class TwoRockPage(Page):
    content = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("content")
    ]


class ContactPage(TwoRockPage):
    def get_context(self, request, *args, **kwargs):
        context = super(ContactPage, self).get_context(request)
        context.update({
            "contact_form": TwoRockContactForm(request=request),
        })
        return context
