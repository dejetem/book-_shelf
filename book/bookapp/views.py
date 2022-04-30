from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView,UpdateAPIView
from .models import Book, Category, Comment
from .serializers import BookSerializer,CategorySerializer,CommentSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class BookList(ListAPIView):

    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_archived']

class BookArchived(UpdateAPIView):
    

    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)
     
    lookup_field = "id"
    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookPost(CreateAPIView):

    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookListCategory(ListAPIView):

    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_archived', 'categories']

class BookDetailView(ListAPIView):

    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)
    #lookup_field = "id"

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_archived', 'id']


class BookListEvery(ListAPIView):

    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_archived']

class BookListEveryCategory(ListAPIView):

    serializer_class = BookSerializer
    #lookup_field = "categories"

    def get_queryset(self):
        return Book.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_archived', 'categories']

class BookDetailViewEvery(ListAPIView):

    serializer_class = BookSerializer
    #lookup_field = "id"

    def get_queryset(self):
        return Book.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_archived', 'id']







class CommentList(CreateAPIView):

    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Comment.objects.filter(parent=self)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_archived']

class CommentListEvery(ListAPIView):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        return Comment.objects.filter(parent=self)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_archived']











