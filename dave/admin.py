from django.contrib import admin
from dave.models import Page, Post, Project, Image

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

class ProjectAdmin(admin.ModelAdmin):
    pass

class ImageAdmin(admin.ModelAdmin):
    list_display: ('name', 'image')

# Register your models here.
admin.site.register(Page, PageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Image, ImageAdmin)
