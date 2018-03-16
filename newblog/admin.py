from django.contrib import admin

# Register your models here.
from .models import Post,Category,Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','creat_time','modified_time','category','auther']
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
