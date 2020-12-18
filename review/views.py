from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from django.contrib import messages
from products.models import Product
from .forms import ReviewForm


def view_review(request, product_id):
    """"
    Gets the id of the product& searches for all reviews
    connected to it and compiles them in review_list which is returned
    to the template
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


def review_form(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    review_list = Review.objects.all().filter(product=product)
    """
    When form is submitted, function is called
    and is given the product_id as an argument.
    The validity of the form is checked and the review is added
    to the database.
    """

    if request.method == "POST":
        new_review = ReviewForm(request.POST)
        if new_review.is_valid():
            new_review.instance.product = product
            new_review.instance.name = request.POST.get('name')
            new_review.instance.review_text = request.POST.get('review_text')
            new_review.save()
            messages.success(request, "Thankyou for submitting a review!")

            template = 'review/review.html'
            context = {
                'review_form': ReviewForm(),
                'review_list': review_list,
                'product': product
            }

            return render(request, template, context)
    else:
        new_review = ReviewForm()

    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)
