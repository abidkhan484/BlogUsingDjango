from django.contrib import admin

from first_app.models import BlogPost, Category


class BlogPostAdmin(admin.ModelAdmin):
    list_filter = ['created_at']
    search_fields = ['title', 'body']
    list_display = ['title', 'category']


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
