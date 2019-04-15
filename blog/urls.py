from django.urls import path
""" Djangoのpath関数をimportする。"""
from . import views
""" blogアプリのすべてのviewをインポートする。"""

"""post_listという名前のviewをルートURLに割り当てる。"""
"""Webサイトにアクセスしてきた最初の人はここに誘導される。"""
"""int:pk 整数の値を期待し、その値がpkという名前の変数でビューに渡されることを意味しています。"""
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
