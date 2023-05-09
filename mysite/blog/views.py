from django.shortcuts import render
<<<<<<< HEAD

def post_list(request):
    return render(request, 'blog/post_list.html', {})

=======
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):   
    post = get_object_or_404(Post, pk=pk)   
    return render(request, 'blog/post_inhoud.html', {'post': post})
>>>>>>> 3473de8e13734d37b0a85cd217659aa8fddd9499

# Create your views here.
