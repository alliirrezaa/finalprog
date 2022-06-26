from django.shortcuts import render,redirect
from .models import *
from cart.models import Cart
from django.utils.crypto import get_random_string
from home.models import Product,Category
from django.core.mail import EmailMessage
from accounts.models import Profile    

def order_create(request):
    if request.method =='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            code=get_random_string(length=8)
            order=Order.objects.create(user_id=request.user.id,first_name=data['first_name'],last_name=data['last_name']
                        ,phone=data['phone'],address=data['address'],postal_code=data['postal_code'],email=data['email']
                        ,code=code
                    )
            cart=Cart.objects.filter(user_id=request.user.id)
            for c in cart:
                OrderItem.objects.create(order_id=order.id,product_id=c.product_id,quantity=c.quantity)
            return redirect('order:factor',order.id)

def payment(request,order_id):
    order=Order.objects.get(id=order_id)
    order.paid=True
    order.save()
    cart=OrderItem.objects.filter(order_id=order_id)
    for x in cart:
        product=Product.objects.get(id=x.product.id)
        product.amount -= x.quantity
        product.save()
    return render(request,'order/payment.html',{'order':order})

def factor(request,order_id):
    cart=Cart.objects.filter(user_id=request.user.id)
    user=request.user
    category=Category.objects.all()
    product=Product.objects.all()
    order=Order.objects.get(id=order_id)
    total=0
    for p in cart:
        total += p.product.price * p.quantity

    if order.paid==True:
        subject='Order status'
        email=order.email
        msg='Your order has been successfully registered.Click the following link to see the factor.'
        body=subject+'\n'+email+'\n'+msg
        form=EmailMessage('Order',body,'tt.alireza.st.kh@gmail.com',(email,))
        EmailMessage()
        form.send(fail_silently=False)

    return render(request,'order/factor.html',{'order':order,'cart':cart,'total':total,'user':user,'category':category})