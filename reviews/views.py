from django.shortcuts import render, redirect


def reviews(request):
    """ A view that renders the review posts in list format """

    reviews = Reviews.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/reviews.html', context)


def add_review(request):

    return render(request, 'reviews/add_review.html')
