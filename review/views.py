from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from django.contrib import messages
from products.models import Product
from .forms import ReviewForm


def review_form(request, product_id):
    "A view that returns the contact page"
    review_form = ReviewForm()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid:
            review_form.save()
            messages.success(request, 'Thank you for submitting that review.')
            return redirect('review')

    template = 'review/review.html'

    context = {
        'review_form': review_form,
        'on_profile_page': True
    }

    return render(request, template, context)


# Create your views here.
def view_review(request, product_id):
    """"
    Gets the id of the specific product and searches for all reviews
    connect to it and puts them in review_list which is then returned
    to the template (review.html)
    """
    product = get_object_or_404(Product, pk=product_id)
    review_list = Review.objects.all().filter(product=product)
    template = 'review/review.html'
    context = {
        'review_list': review_list,
        'product': product
    }

    return render(request, template, context)
