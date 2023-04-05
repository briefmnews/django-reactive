from django.forms import JSONField
from django.forms import CharField

from .widgets import ReactJSONSchemaFormWidget, TemplateFormWidget


class ReactJSONSchemaFormField(JSONField):
    widget = ReactJSONSchemaFormWidget


class TemplateFormField(CharField):
    widget = TemplateFormWidget
