from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('author', {'fields': ['author']}),
        ('title', {'fields': ['title']}),
        ('text', {'fields': ['text']}),
        ('published_date', {'fields': ['published_date']}),
    ]

admin.site.register(Post, PostAdmin)
