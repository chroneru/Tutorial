from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.

def index_view(request):
    posts_all = Post.objects.all()
    context = {'posts_all': posts_all}
    return render(request, 'tutor/index.html', {'posts_all': posts_all})

def each_view(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'tutor/tutor_detail.html', {'post': post})
