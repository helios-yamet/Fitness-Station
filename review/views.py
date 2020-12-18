from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from django.contrib import messages
from products.models import Product
from .forms import ReviewForm


def review_form(request, product_id):
    "A view that returns the review page"
    review_form = ReviewForm()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid:
            review_form.save()
            messages.success(request, 'Thank you for submitting that review.')
            return redirect('view_review')

            template = 'review/review.html'

            context = {
                'review_form': ReviewForm(),
                'on_profile_page': True
            }

    return render(request, template, context)


def view_review(request, product_id):
    """"
    Gets the id of the product and searches all reviews
    connected to it, and attatches them in a review_list
    which is returned to the template.
    """
    product = get_object_or_404(Product, pk=product_id)
    review_list = Review.objects.all().filter(product=product)
    template = 'review/review.html'
    context = {
        'review_form': ReviewForm(),
        'review_list': review_list,
        'product': product
    }

    return render(request, template, context)
