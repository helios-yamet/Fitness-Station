from django.shortcuts import render
from .models import Product


# Create your views here.


def index(request):
    """ A view to return the index page """
    products = Product.objects.filter()
    query = None
    categories = None
    sort = None
    direction = None

    return render(request, 'home/index.html')
