from datauri import DataURI, InvalidDataURI
from jsonpointer import resolve_pointer, JsonPointerException

from django.shortcuts import get_object_or_404
from django.views import View
from django.http import HttpResponse, Http404


class URIImageAsFileView(View):
    model_class = None
    field_name = None

    def get(self, request, pk, pointer, model_class=None, field_name=None):
        """
        :param request:
        :param pk: the pk of the instance
        :param pointer: the json pointer of the image. Ex: "people/image", "people/0/image", etc.
        :param model_class: the model that holds the JSON field
        :param field_name: the JSON-field name
        :return: HttpResponse with the image

        Base view to serve an URI-stored (in a JSON field) image as a file.

        Example usage in urls.py:

            re_path(
                r"some/path/(?P<pk>\d+)/(?P<pointer>.+)/",
                URIImageAsFileView.as_view(),
                kwargs={"model_class": MyModel, "field_name": "my_json_field"},
            ),

        """
        obj = get_object_or_404(model_class or self.model_class, pk=pk)
        data = getattr(obj, field_name or self.field_name)
        pointer = "/{}".format(pointer)
        try:
            data = resolve_pointer(data, pointer)
            uri = DataURI(data)
            return HttpResponse(uri.data, content_type=uri.mimetype)
        except (InvalidDataURI, JsonPointerException):
            raise Http404("Image not found")
