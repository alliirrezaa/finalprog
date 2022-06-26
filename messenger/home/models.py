from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.forms import ModelForm

class Category(models.Model):
    sub_category=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='sub_cat')
    sub=models.BooleanField(default=False)
    name=models.CharField(max_length=200)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    slug=models.SlugField(allow_unicode=True,unique=True,null=True)
    image=models.ImageField(upload_to='category',null=True,blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ManyToManyField(Category)
    name=models.CharField(max_length=200)
    amount=models.PositiveBigIntegerField()
    available=models.BooleanField(default=True)
    price=models.PositiveBigIntegerField()
    information=RichTextField(blank=True,null=True)
    extra_information=RichTextField(blank=True,null=True)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='product')
    like=models.ManyToManyField(User,blank=True,related_name='prod_like')
    total_like=models.PositiveIntegerField(default=0)
    dislike=models.ManyToManyField(User,blank=True,related_name='prod_dislike')
    total_dislike=models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name
    
    def total_like(self):
        return self.like.count()
    
    def total_dislike(self):
        return self.dislike.count()
    
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    comment=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    reply=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='comment_reply')
    is_reply=models.BooleanField(default=False)

    def __str__(self):
        return self.product.name

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['comment']

class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images')

class Gallery(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to='gallery',blank=True)

    def __str__(self):
        return self.name
