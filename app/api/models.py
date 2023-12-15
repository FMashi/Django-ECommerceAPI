from django.db import models
##Create your models here.

class Customers(models.Model):
   CustomersID = models.IntegerField(primary_key=True)
   FirstName = models.CharField(max_length=100)
   LastName = models.CharField(max_length=100)

   def __str__(self):
       return self.CustomersID

class Products(models.Model):
    ProductID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()

    def __str__(self):
        return self.ProductID


class Orders(models.Model):
    OrdersID = models.IntegerField(primary_key=True)
    Customers_ID=models.ForeignKey(Customers,on_delete=models.CASCADE)
    Product_ID=models.ForeignKey(Products,on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    CreatedAt=models.DateField()


    def __str__(self):
       return self.OrdersID

class Reviews(models.Model):
    ReviewID = models.IntegerField(primary_key=True)
    Customers_ID=models.ForeignKey(Customers,on_delete=models.CASCADE)
    Product_ID=models.ForeignKey(Products,on_delete=models.CASCADE)
    Rating=models.IntegerField()
    Review=models.TextField()

    def __str__(self):
       return self.ReviewID








