# -*- encoding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import Site
from django import template
register = template.Library()

@register.simple_tag
def site_name():
    current_site = Site.objects.get_current()
    return current_site.name

@register.simple_tag
def site_domain():
    current_site = Site.objects.get_current()
    return current_site.domain