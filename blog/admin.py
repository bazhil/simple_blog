#  coding: utf-8

from django.contrib import admin

# Register your models here.
from blog.models import BlogPost, BlogPostAdmin

admin.site.register(BlogPost, BlogPostAdmin)