from django import template
import json

register = template.Library()

@register.filter
def micro_to_milli(value):
    return value/1000

@register.filter
def render_twill(result):
    return result.test.render(result.site)

@register.filter
def to_json(value):
    return json.dumps(value)
