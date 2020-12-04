from django.shortcuts import render, context

# Create your views here.


def blogo(request):
    """ A view to return the blog page """

    return render(request, 'blog/blog.html', context)
