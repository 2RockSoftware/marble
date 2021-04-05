from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class FounderBlock(blocks.StructBlock):
    name = blocks.CharBlock(max_length=255)
    bio = blocks.TextBlock()
    image = ImageChooserBlock("image")

    def __str__(self):
        return self.name

    class Meta:
        template = "cms/blocks/founder.html"

    @property
    def title(self):
        return "Founder"


class DeveloperBlock(blocks.StructBlock):
    name = blocks.CharBlock(max_length=255)
    bio = blocks.TextBlock()
    image = ImageChooserBlock()

    def __str__(self):
        return self.name

    class Meta:
        template = "cms/blocks/developer.html"

    @property
    def title(self):
        return "Developer"


class ProjectBlock(blocks.StructBlock):
    name = blocks.CharBlock(max_length=255)
    description = blocks.TextBlock()
    widget = blocks.TextBlock()
    code = blocks.TextBlock()

    def __str__(self):
        return self.name

    class Meta:
        template = "cms/blocks/project.html"


class ClientsLogos(blocks.StructBlock):
    logo_1 = ImageChooserBlock()
    logo_2 = ImageChooserBlock()
    logo_3 = ImageChooserBlock()
    logo_4 = ImageChooserBlock()

    class Meta:
        template = "cms/blocks/clients_logos.html"
