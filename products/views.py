from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries.
    Create and attach all product object and search objects = none.
    Create get sort, attach sortkey to request.
    Instruct if product or category name is requested.
    Return product or category and list in descending order.
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            """
            If user enter invalid search,
            return error page with error message.
            """
            query = request.GET["q"]
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) |\
                Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """ A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """login required to complete this action.
    Add a product to the Gym,
    if user does not have superuser privelege,
    return error.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Gym owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        """
        If request to post product is valid, return success message.
        """
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            """
            If request invalid, return error message,
            product is not added.
            """
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """login required to complete this action.
    Edit a product,
    only superuser can do this.
    If not a superuser, error message is returned.
    Redirected to homepage.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Gym owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        """
        Superuser submits valid product update,
        return success message.
        """
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            """
            If invalid product update,
            return error message.
            """
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """login required to complete this action.
    Delete a product from the Gym,
    only superusers can delete products.
    If superuser submits valid form, product is submitted.
    Return product deleted.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Gym owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
