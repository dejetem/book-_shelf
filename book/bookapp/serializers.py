from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Book, Category, Comment



class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        verbose_name_plural='Categories'

        fields = ['name', 'id', 'slug']
    def __str__(self):
        return self.name


class CommentSerializer(ModelSerializer):
    owner = SerializerMethodField()
    class Meta:
        model = Comment
        ordering = '-id'

        fields = ['post', 'id', 'owner', 'description', 'date_added']
    def get_owner(self, obj):
        return obj.owner.username

class BookSerializer(ModelSerializer):
    comments = CommentSerializer(source='comments.description')
    owner = SerializerMethodField()
    book_cover = SerializerMethodField()
    
    class Meta:
        model = Book
        ordering = '-id'

        fields = ['owner', 'id', 'author', 'title', 'description',
                  'book_cover', 'publication_date', 'is_archived', 'categories', 'comments']
    def get_book_cover(self, obj):
        try:
            book_cover = obj.book_cover.url
        except:
            book_cover = None
        return book_cover

    def get_owner(self, obj):
        return obj.owner.username
