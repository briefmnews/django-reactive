from django.contrib.postgres.forms.jsonb import JSONField
from django.forms import CharField

from .widgets import ReactJSONSchemaFormWidget, TemplateFormWidget


class ReactJSONSchemaFormField(JSONField):
    widget = ReactJSONSchemaFormWidget


class TemplateFormField(CharField):
    widget = TemplateFormWidget
