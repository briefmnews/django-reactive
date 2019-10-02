import json

from django.conf import settings
from django.forms.widgets import Widget
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
            settings.STATIC_URL + 'dist/react-16.6.3.js',
            settings.STATIC_URL + 'dist/react-dom-16.6.1.js',
            settings.STATIC_URL + 'dist/react-jsonschema-form.js',
            settings.STATIC_URL + 'js/django_reactive.js',
        )

    template_name = 'django_reactive.html'

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
