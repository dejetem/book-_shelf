from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=255)
  slug = models.SlugField(max_length=255, unique=True)
  
  class Meta:
    verbose_name_plural='Categories'
    
  def __str__(self):
    return self.name

class Book(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    book_cover = models.URLField(null=True)
    publication_date = models.DateField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)
    categories = models.ForeignKey(Category, related_name="categories", on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' |' + str(self.owner)


class Comment(models.Model):
    post = models.ForeignKey(Book, related_name="comments", on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner