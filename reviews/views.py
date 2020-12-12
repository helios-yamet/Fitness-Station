from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


def reviews(request):
    """ A view that renders the blog posts in list format """

    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'reviews/reviews.html', context)


def add_review(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'reviews/add_review.html', context)
