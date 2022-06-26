from django.db import models
from django.contrib.auth.models import User
from home.models import Product
from django.forms import ModelForm

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    create=models.DateTimeField(auto_now_add=True)
    paid=models.BooleanField(default=False)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.IntegerField()
    address=models.CharField(max_length=500)
    postal_code=models.IntegerField()
    email=models.EmailField()
    code=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.user.username

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def __str__(self):
        return self.product.name

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=['email','first_name','last_name','address','phone','postal_code']