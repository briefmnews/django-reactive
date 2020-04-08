from datauri import DataURI, InvalidDataURI
from jsonpointer import resolve_pointer, JsonPointerException

from django.shortcuts import get_object_or_404
from django.views import View
from django.http import HttpResponse, Http404


class URIImageAsFileView(View):
    model = None
    field = None

    def get(self, request, pk, pointer):
        """
        :param request:
        :param pk: the pk of the instance
        :param pointer: the json pointer of the image. In the form "image", "people/image" or
        "people/0/image"
        :return: HttpResonse with the image

        Base view to serve an URI-stored (in a JSON field) image as a file.
        """
        obj = get_object_or_404(self.model, pk=pk)
        data = getattr(obj, self.field)
        pointer = "/{}".format(pointer)
        try:
            data = resolve_pointer(data, pointer)
            uri = DataURI(data)
            return HttpResponse(uri.data, content_type=uri.mimetype)
        except (InvalidDataURI, JsonPointerException):
            raise Http404("Image not found")
