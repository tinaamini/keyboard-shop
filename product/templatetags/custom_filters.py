from django import template

register = template.Library()

@register.filter
def iran_currency(value):
    try:
        value = int(value)
        # Format the number with Persian commas
        return "{:,.0f}".format(value).replace(',', '٬') 
    except (ValueError, TypeError):
        return value