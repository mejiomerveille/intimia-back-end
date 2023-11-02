from django.contrib import admin

# Register your models here.
from .models import *

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('nom', 'photo', 'bio')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nom',  'slug')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'intro', 'slug', 'date_added')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'email', 'date_added')    


admin.site.register(CreateBlog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
