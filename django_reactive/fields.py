from django.db.models import CharField, JSONField

from .forms.fields import ReactJSONSchemaFormField, TemplateFormField
from .forms.widgets import ReactJSONSchemaFormWidget, TemplateFormWidget


class ReactJSONSchemaField(JSONField):

    def __init__(self, template=None, **kwargs):
        kwargs.setdefault('default', dict)
        super(ReactJSONSchemaField, self).__init__(**kwargs)
        self.template = template

    def formfield(self, **kwargs):
        defaults = {
            'required': not self.blank,
        }
        defaults.update(**kwargs)
        return ReactJSONSchemaFormField(
            widget=ReactJSONSchemaFormWidget(
                template=self.template
            ),
            **defaults
        )


class TemplateField(CharField):
    def __init__(self, templates=None, **kwargs):
        kwargs.setdefault("default", "")
        self.templates = templates
        if self.templates:
            choices = []
            if kwargs.get("blank"):
                choices.append(("", "------"))
            choices.extend([(name, label) for (name, label, schema) in templates])
            kwargs['choices'] = choices
            self.templates = {name: schema for (name, label, schema) in templates}
        super(TemplateField, self).__init__(**kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'required': not self.blank,
        }
        defaults.update(**kwargs)
        return TemplateFormField(
            widget=TemplateFormWidget(choices=self.choices, templates=self.templates),
            **defaults
        )
