from django.contrib import admin
from . models import *

class ItemInline(admin.TabularInline):
    model=OrderItem
    readonly_feilds=['product','quantity']

class OrderAdmin(admin.ModelAdmin):
    list_display=['user','first_name','last_name','address','email','create','paid','code']
    inlines=[ItemInline]
    
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)