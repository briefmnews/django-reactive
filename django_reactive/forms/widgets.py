import json

from django.conf import settings
from django.forms.widgets import Widget, Select
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class ReactJSONSchemaFormWidget(Widget):
    class Media:
        css = {
            'all': (
                settings.STATIC_URL + 'css/django_reactive.css',
            )
        }
        js = (
            settings.STATIC_URL + 'dist/react.js',
            settings.STATIC_URL + 'dist/react-dom.js',
            settings.STATIC_URL + 'dist/react-jsonschema-form.js',
            "https://cdn.tiny.cloud/1/qagffr3pkuv17a8on1afax661irst1hbr4e6tbv888sz91jc/tinymce/5/tinymce.min.js",
            settings.STATIC_URL + 'dist/custom.js',
            settings.STATIC_URL + 'js/django_reactive.js',
        )

    template_name = 'django_reactive/django_reactive.html'

    def __init__(self, template, **kwargs):
        self.template = template
        super(ReactJSONSchemaFormWidget, self).__init__(**kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        context = {
            'data': value,
            'name': name,
            'template': self.template,
        }

        return mark_safe(render_to_string(self.template_name, context))


class TemplateFormWidget(Select):
    template_name = 'django_reactive/widgets/select_templates.html'
    # option_template_name = 'django/forms/widgets/select_option.html'

    def __init__(self, templates, **kwargs):
        self.templates = templates
        super(TemplateFormWidget, self).__init__(**kwargs)

    def get_context(self, name, value, attrs):
        context = super(TemplateFormWidget, self).get_context(name, value, attrs)
        context["templates"] = self.templates
        return context
