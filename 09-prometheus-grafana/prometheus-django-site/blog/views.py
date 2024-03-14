from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

from .models import Post


def index(request):
    posts_list = Post.objects.filter(active=True).order_by('-id')
    paginator = Paginator(posts_list, 9)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'index.html', {'posts': posts})


def show(request, post_id):
    post = Post.objects.get(pk=post_id)
    if not post.active:
        raise Http404

    return render(request, 'show.html', {'post': post})
