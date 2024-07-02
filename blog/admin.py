from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'text']
    list_filter = ('author', 'created_date', 'published_date')

admin.site.register(Post, PostAdmin)