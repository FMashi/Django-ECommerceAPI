from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


Grade = [
    ('excellent', 1),
    ('average', 0),
    ('bad', -1)
]



class CustomUser(AbstractUser):
   email = models.EmailField(unique=True)
   
   def __str__(self):
       return self.username
   
@receiver(post_save, sender=CustomUser)
def create_user_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_customer(sender, instance, **kwargs):
    instance.customer.save()


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    first_name = models.CharField(max_length=50, blank=True, null=True )
    last_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.quantity} {self.product.name} by {self.customer.first_name}"

class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.CharField(choices=Grade, default='average', max_length=50)
    review = models.TextField()

    def __str__(self):
        return f"Review by {self.customer.first_name} for {self.product.name}"
