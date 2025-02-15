from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Category, Post


def index(request):
    post_list = Post.published.all()[:settings.POSTS_ON_PAGE]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, id):
    post = get_object_or_404(Post.published.all(), pk=id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(is_published=True), slug=category_slug
    )
    post_list = category.posts(manager='published').all()

    return render(request, 'blog/category.html',
                  {'category': category, 'post_list': post_list})
