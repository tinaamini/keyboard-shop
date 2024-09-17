from django import template

register = template.Library()

@register.filter
def iran_currency(value):
    try:
        value = int(value)
        # Format the number with Persian commas
        formatted_value = "{:,.0f}".format(value).replace(',', '٬')

        # Replace English digits with Persian digits
        persian_digits = {'0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'}
        for en_digit, fa_digit in persian_digits.items():
            formatted_value = formatted_value.replace(en_digit, fa_digit)

        return formatted_value
    except (ValueError, TypeError):
        return value