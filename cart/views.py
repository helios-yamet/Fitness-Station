from django.shortcuts import render, redirect


def view_cart(request):
    """ A view that renders the shopping cart content """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """Add a quantity to a specific product to the shopping cart"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
