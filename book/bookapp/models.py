from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=255, blank=False, default='')
  owner = models.ForeignKey(to=User, related_name='categories', on_delete=models.CASCADE)
  books = models.ManyToManyField('Book', related_name='categories', blank=True)

  
 

class Book(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    book_cover = models.URLField()
    publication_date = models.DateField()
    is_archived = models.BooleanField(default=False)

    def __str__(self):
      return self.title + ' | ' + str(self.owner)

    def get_absolute_url(self):
        #return reverse('post-detail')
      return reverse('home')



class Comment(models.Model):
    post = models.ForeignKey(to=Book, related_name="comments", on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, related_name="comments", on_delete=models.CASCADE)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Comment by {self.owner.username} on {self.post}'

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

