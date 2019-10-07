from django.contrib.postgres.fields import JSONField as BaseJSONField
from django.db.models import CharField

from .forms.fields import ReactJSONSchemaFormField, TemplateFormField
from .forms.widgets import ReactJSONSchemaFormWidget, TemplateFormWidget


class ReactJSONSchemaField(BaseJSONField):

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
        kwargs.setdefault('default', dict)
        self.templates = templates
        if self.templates:
            kwargs['choices'] = [(t[0], t[1]) for t in templates]
            self.templates = {t[0]: t[2] for t in templates}
        super(TemplateField, self).__init__(**kwargs)

    def formfield(self, **kwargs):
        return TemplateFormField(
            widget=TemplateFormWidget(choices=self.choices, templates=self.templates),
            **kwargs
        )
