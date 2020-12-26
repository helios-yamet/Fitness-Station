from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculate product price& quantity,
    return subtotal.
    """
    return price * quantity
