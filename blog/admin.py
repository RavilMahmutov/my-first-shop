from django.contrib import admin
from .models import Post, Good, Category


admin.site.register(Post)
admin.site.register(Good)
admin.site.register(Category)