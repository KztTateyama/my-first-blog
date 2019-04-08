from django.shortcuts import render
from django.utils import timezone

from .models import Post
""" カレントディレクトリにある「model.py」に定義している Postオブジェクトを使う"""


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    """ 「published_date」の昇順にリストを並べ替える。"""
    return render(request, 'blog/post_list.html', {'posts': posts})

