from django import template
from django.contrib.sessions.backends.db import SessionStore

from users.extra.google import Google

register = template.Library()

@register.simple_tag
def url_in():
    return Google.url_in()
