from django.contrib import admin
from .models import Blog


# Register your models here.
class display_blog(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_text', 'blog_Img', 'blog_date', 'BlogUpdate_date')

admin.site.register(Blog, display_blog)