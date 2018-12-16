from django.urls import path
""" Djangoのpath関数をimportする。"""
from . import views
""" blogアプリのすべてのviewをインポートする。"""

"""post_listという名前のviewをルートURLに割り当てる。"""
"""Webサイトにアクセスしてきた最初の人はここに誘導される。"""
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
