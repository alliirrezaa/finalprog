from django.contrib import admin
from .models import *

class CartAdmin(admin.ModelAdmin):
    list_display=['user','product','quantity']

admin.site.register(Cart,CartAdmin)
