from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=255)
  
 

class Book(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    book_cover = models.URLField()
    publication_date = models.DateField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)
    categories = models.ForeignKey(Category, related_name="categories", on_delete=models.CASCADE)



class Comment(models.Model):
    post = models.ForeignKey(Book, related_name="comments", on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

