from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models.functions import Lower

from .models import Product, Category


# Create your views here.


def index(request):
    """ A view to return the index page.
    Create product object filter function,
    variables = none and return product context
    and render homepage template.
     """
    products = Product.objects.filter()
    query = None
    categories = None
    sort = None
    direction = None

    context = {"products": products}

    return render(request, 'home/index.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details.
    Create instance of product and get product id.
    Return rendered edit product template.
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)
