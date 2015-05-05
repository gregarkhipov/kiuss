from django import template
import urllib

register = template.Library()

@register.simple_tag
def timebyip():
    return "nil"

@register.assignment_tag
def longlat(qs):
    return qs.exclude(latitude__isnull=True, longitude__isnull=True).exclude(latitude__exact="", longitude__exact="")
