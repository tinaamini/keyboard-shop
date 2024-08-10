from django import template

register = template.Library()

@register.filter
def iran_currency(value):
    try:
        value = int(value)
        return "{:,}".format(value)
    except (ValueError, TypeError):
        return value