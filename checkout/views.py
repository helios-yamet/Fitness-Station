from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_live_51Hs54nJRE250pDbbTtQVDIj4pjggXEsKgrUY1wrpByCkucTM4HDjHOHkLXvFScX7e1v73I2h7n937GWJCSZyxWch00P8GIMFld',
        'client_secret': 'Test client secret',
    }

    return render(request, template, context)
