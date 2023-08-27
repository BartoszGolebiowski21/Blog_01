from django.contrib import admin

from .models import Author, Post, Tag, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "date", "tags",)
    list_display = ("title", "date", "author",)

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
