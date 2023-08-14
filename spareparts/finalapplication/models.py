from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
# we are accessing a registration user model.
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Create your models here.
# category is inheriting from models.Model
# registration form for users.

# class userProfile(AbstractUser):
#     username= models.CharField(max_length=100,unique=True,null=False,blank=False)
#     email= models.EmailField(unique=True,null=False,blank=True)
#     phone = models.CharField(max_length=50,null=False,blank=True,unique=True)
#     def __str__(self):
#         return self.username
#     class Meta:
#         db_table='spare_users'
#         verbose_name='User'
#         verbose_name_plural='Users'












class Category(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False,unique=True)

    def __str__(self):
        return self.name
# defining a model for product

class Product(models.Model):
    #linking the product to the category(referencing)
    # here the foriegn key is name.
    # on_delete cascade deletes the category and the products related.
    Category_name=models.ForeignKey(Category, on_delete=models.CASCADE,null=False,blank=False)
    item_name=models.CharField(max_length=50,null=False,blank=False)
    date_of_arrival = models.DateField(default=timezone.now)
    country_of_origin=models.CharField(max_length=50,null=False,blank=False)
    total_quantity=models.IntegerField(default=0,null=False,blank=False,validators=[MinValueValidator(1)])
    issued_quantity=models.IntegerField(default=0,null=False,blank=False)
    received_quantity=models.IntegerField(default=0,null=False,blank=False)
    unit_price=models.IntegerField(default=0,null=False,blank=False)


    def __str__(self):
        return self.item_name

#defining a model for sales

class Sale(models.Model):
    item = models.ForeignKey(Product,on_delete=models.CASCADE,null=False,blank=False)
    date_of_sale = models.DateField(default=timezone.now)
    contact=models.CharField(max_length=50,null=False, blank=False)
    branch_name=models.CharField(max_length=50,null=False,blank=False)
    quantity=models.IntegerField(default=0,null=False, blank=False)
    amount_received = models.IntegerField(default=0,null=False, blank=False)
    issued_to=models.CharField(max_length=100,null=False, blank=False)#buyer
    part_name=models.CharField(max_length=50,null=False, blank=False)
    unit_price=models.IntegerField(default=0,null=False, blank=False)#for installments.
    


class MyImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')





    # the sales made so far(total)
    def get_total(self):
        total=self.quantity*self.item.unit_price  
        return int(total)

# here we are getting change.(money to be given to the customer)
    def get_change(self):
        change=self.get_total() - self.amount_received
        return abs(int(change))
    
    def __str__(self):
        return self.item.item_name # sales is linked to products.



    