from django.shortcuts import render, get_object_or_404

from .models import Post, Category

from django.utils import timezone

POSTS_PER_PAGE = 5


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.get_published_posts()[:POSTS_PER_PAGE]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        pk=id,
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )
    context = {
        'post': post
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = Post.objects.get_published_posts().filter(category=category)
    context = {'post_list': post_list, 'category_slug': category_slug}
    return render(request, template, context)
