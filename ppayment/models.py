from django.db import models
from django.contrib.auth.models import User
#from django.datetime import datetime

class Product(models.Model):
    sellerId = models.IntegerField()
    productName = models.CharField(max_length = 128)
    amount = models.IntegerField()

    def __getPid__(self):
        return self.id
    def __getAmount__(self):
        return self.amount
    def __getSellerId__(self):
        return self.sellerId

class Notification(models.Model):
    timeStamp = models.DateTimeField(auto_now_add=True)
    #productId = models.ForeignKey(Product, related_name = 'Notification_productIds', null=False)
    #amount = models.ForeignKey(Product, related_name = 'Notification_amounts', null=False)
    sellerId = models.IntegerField()
    productId = models.IntegerField()
    amount = models.IntegerField()
    buyerName = models.CharField(max_length = 128, default = 'ABC')
    shippingAddr = models.CharField(max_length = 128, default = 'XYZ')
    # Return the notification dictionary
    def __notify__(self):
        return self.timeStamp
    def __sellerId__(self):
        return self.id
