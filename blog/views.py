from django.views import redirect, reverse
from .models import Post, render, redirect
from .forms import PostForm


def PostList(request, ListView):
    """ A view that renders the blog posts in list format """

    queryset = Post.objects.filter(status=1).order_by('-created_on')
    return render(redirect('blog/blog_index.html'))


def PostDetail(request, DetailView):
    """ A view that renders individual blog post detail """

    model = Post
    return render(redirect('blog/post_detail.html'))


def AddPostView(request, CreateView):
    """ A view that render an add new blog post form page"""

    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

    return redirect(reverse('blog'))
