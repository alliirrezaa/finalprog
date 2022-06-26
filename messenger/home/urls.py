from django.urls import path
from . import views
 
app_name='home'

urlpatterns = [
    path('', views.main, name='main'),
    path('contact/',views.contact,name='contact'),
    path('products/',views.productss,name='productss'),
    path('detail/<int:id>',views.product_detail,name='product_detail'),
    path('category/<slug:slug>',views.productss,name='category'),
    path('like/<int:id>/',views.product_like,name='product_like'),
    path('dislike/<int:id>/',views.product_dislike,name='product_dislike'),
    path('comment/<int:id>/',views.product_comment,name='product_comment'),
    path('comment/<int:id>/<int:comment_id>/',views.reply_comment,name='reply_comment'),
    path('search/',views.productss,name='product_search'),
]