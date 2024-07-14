from django.db import models



class Book(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    authors = models.CharField(max_length=255,blank=True,null=True)
    publisher = models.CharField(max_length=255,blank=True,null=True)
    published_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True,null=True)
    isbn_13 = models.CharField(max_length=13, unique=True)
    page_count = models.IntegerField(blank=True,null=True)
    thumbnail_url = models.URLField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title
