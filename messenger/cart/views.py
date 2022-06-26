from django.shortcuts import render,redirect
from home.models import Product,Category
from accounts.models import Profile
from .models import *
from django.contrib.auth.decorators import login_required
from order.models import OrderForm

def cart_detail(request):
    cart=Cart.objects.filter(user_id=request.user.id)
    profile=Profile.objects.get(user_id=request.user.id)
    category=Category.objects.all()
    product=Product.objects.all()
    form=OrderForm()
    user=request.user
    total=0
    for p in cart:
        total += p.product.price * p.quantity
    return render(request,'cart/cart.html',{'cart':cart,'total':total,'form':form,'user':user,'category':category})

@login_required(login_url='accounts:user_login')
def add_cart(request,id):
    url=request.META.get('HTTP_REFERER')
    product=Product.objects.get(id=id)
    data=Cart.objects.filter(user_id=request.user.id,product_id=id)
    if data:
        check='yes'
    else:
        check='no'
    if request.method == 'POST':
        form=CartForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data['quantity']
            if check=='yes':
                shop=Cart.objects.get(user_id=request.user.id,product_id=id)
                shop.quantity += info
                shop.save()
            else:
                Cart.objects.create(user_id=request.user.id,product_id=id,quantity=info)
    return redirect(url)

@login_required(login_url='accounts:user_login')
def remove_cart(request,id):
    url=request.META.get('HTTP_REFERER')
    Cart.objects.filter(id=id).delete()
    return redirect(url)

def add_single(request,id):
    url=request.META.get('HTTP_REFERER')
    cart=Cart.objects.get(id=id)
    product=Product.objects.get(id=cart.product.id)
    if product.amount > cart.quantity:
        cart.quantity +=1
    cart.save()
    return redirect(url)

def remove_single(request,id):
    url=request.META.get('HTTP_REFERER')
    cart=Cart.objects.get(id=id)
    if cart.quantity==1:
        cart.delete()
    else:
        cart.quantity -=1
        cart.save()
    return redirect(url)