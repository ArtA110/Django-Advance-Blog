from django.contrib import admin
from .models import Post, Category

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "status", "category"]
    list_filter = ["author", "status"]
    search_fields = ("content",)


admin.site.register(Post)
admin.site.register(Category)
