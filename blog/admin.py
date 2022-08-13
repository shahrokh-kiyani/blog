from django.contrib import admin

from .models import Category, Post


# Registerd category in admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

# Registerd Post in admin and filterd by list_display
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'modified_date', 'category')

