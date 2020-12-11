from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


def blog(request):
    """ A view that renders the blog posts in list format """

    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'blog/blog.html', context)


def add_blog_post(request):
    if request.method == 'POST':
        title = request.POST.get('item_title')
        content = request.POST.get('item_content')

        Item.objects.create(title=title, content=content)
        return redirect('blog')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'blog/add_post.html', context)


def edit_blog_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('blog')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'blog/edit_post.html', context)


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('blog')
