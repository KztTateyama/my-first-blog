from django.contrib import admin
"""models.pyで定義したPostをインポートしている。"""
from .models import Post

admin.site.register(Post)

# Register your models here.
