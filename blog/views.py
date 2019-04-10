from django.shortcuts import render
from django.utils import timezone

from .models import Post
""" カレントディレクトリにある「model.py」に定義している Postオブジェクトを使う"""


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    """ 「published_date」の昇順にリストを並べ替える。"""
    return render(request, 'blog/post_list.html', {'posts': posts})
    """  renderでテンプレートに渡す。 
         request:　ユーザからインターネットを介して、受け取った情報
         'blog/post_list.html':  テンプレート
         {'posts': posts} :  渡す情報。ここの情報がhtmlに渡される。
    """

