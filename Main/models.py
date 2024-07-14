from django.db import models
# from psutil import users
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    authors = models.CharField(max_length=255,blank=True,null=True)
    publisher = models.CharField(max_length=255,blank=True,null=True)
    published_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True,null=True)
    isbn_13 = models.CharField(max_length=13, unique=True,primary_key=True)
    page_count = models.IntegerField(blank=True,null=True)
    thumbnail_url = models.URLField(max_length=255,blank=True,null=True)
    available = models.IntegerField(default=10)


    def __str__(self):
        return self.title

class Transaction(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    success = models.BooleanField(default=True)
    
class Cart(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class detect_duration(models.Model):
    time_to_return = models.IntegerField(default=7)
    Transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    