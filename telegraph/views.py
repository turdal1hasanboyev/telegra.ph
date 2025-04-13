from django.shortcuts import render, get_object_or_404, redirect

from .models import Post


def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')

        post = Post.objects.create(
            title=title,
            author=author,
            content=content
        )

        return redirect('post_detail', slug=post.slug)

    return render(request, 'create_post.html')


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'post_detail.html', {'post': post})


def edit_post(request, edit_token):
    post = get_object_or_404(Post, edit_token=edit_token)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.author = request.POST.get('author')
        post.content = request.POST.get('content')
        post.save()

        return redirect('post_detail', slug=post.slug)

    return render(request, 'edit_post.html', {'post': post})
