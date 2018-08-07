from django.shortcuts import render
from django.utils import timezone
from .models import Post  # 새로 추가한 거임

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #새로 추가됨
    return render(request, 'blog/post_list.html', {'posts' : posts})