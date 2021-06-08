from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, PostImage
from django.conf import settings
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html')


def contact(request):

    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def blog_view(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})


def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'detail.html', {
        'post': post,
        'photos': photos
    })


@login_required
def create_post_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        link = request.POST.get('link')
        description = request.POST.get('description')

        post = Post.objects.create(
            title=title,
            subtitle=subtitle,
            link=link,
            description=description
        )

        for file_num in range(0, int(length)):
            PostImage.objects.create(
                post=post,
                images=request.FILES.get(f'images{file_num}')
            )

    return render(request, 'create-post.html')
