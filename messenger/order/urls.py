from django.urls import path
from . import views

app_name='order'
urlpatterns = [
    path('create/',views.order_create,name='order_create'),
    path('payment/<int:order_id>/',views.payment,name='payment'),
    path('factor/<int:order_id>/',views.factor,name='factor'),
]
