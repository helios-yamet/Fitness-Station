from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """Add a quantity of the specified product to the cart"""

    quantity = str(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
        cart = request.session.get('cart', {})
        product = Product.objects.get(id=item_id)
        redirect_url = request.POST.get('redirect_url')

# If item has sizes, organize by item_id and then size
    if size:
        if item_id in list(cart.keys()):
            print(cart[item_id])['items_by_size']
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]}')
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')

# Otherwise organize only by item_id
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = str(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})
    product = Product.objects.get(id=item_id)

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]}')
        else:
            del cart[item_id]['items_by_size'][size]
            messages.success(request, f'Removed size {size.upper()} {product.name} from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Set the quantity of the give item to 0"""
    try:
        cart = request.session.get('cart', {})
        product = Product.objects.get(id=item_id)
        size = None
        if 'size' in request.POST:
            size = request.POST['size']
        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
