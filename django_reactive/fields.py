from django.contrib.postgres.fields import JSONField as BaseJSONField

from .forms.fields import ReactJSONSchemaFormField
from .forms.widgets import ReactJSONSchemaFormWidget


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
