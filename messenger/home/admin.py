from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','create','update')
    list_filter=('create',)
    prepopulated_fields={
        'slug':('name',)
    }

class ImagesInlines(admin.TabularInline):
    model=Images
    extra=1
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','create','update','amount','available','price')
    list_filter=('available',)
    inlines=[ImagesInlines]

class CommentAdmin(admin.ModelAdmin):
    list_display=('user','date')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Images)
admin.site.register(Gallery)