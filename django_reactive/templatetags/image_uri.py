from django import template

register = template.Library()


@register.simple_tag
def json_pointer(*args):
    """
    Get a list of strings and int and template them as a "json path"
    exemple:
    {%  image_field "people" 0 'picture' as field %}
    will return
    people/0/picture

    :param args: A list of string and int
    :return: a "json pointer
    """
    return "/".join([str(a) for a in args])
