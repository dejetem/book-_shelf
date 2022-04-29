from rest_framework.serializers import ModelSerializer
from .models import Book, Category, Comment


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        verbose_name_plural='Categories'

        fields = ['name', 'id', 'slug']
    def __str__(self):
        return self.name

class BookSerializer(ModelSerializer):

    class Meta:
        model = Book

        fields = ['owner', 'id', 'author', 'title', 'description',
                  'book_cover', 'publication_date', 'is_archived', 'categories']
    def __str__(self):
        return self.title + ' |' + str(self.owner)

class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment

        fields = ['name', 'id', 'slug']
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)