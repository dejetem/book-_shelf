from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Book, Category, Comment
from .serializers import BookSerializer,CategorySerializer,CommentSerializer
from rest_framework import permissions
# Create your views here.

class BookList(ListCreateAPIView):

    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

class BookDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated)
    lookup_field = ["id", "categories"]

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

class BookListEvery(ListCreateAPIView):

    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter()

class BookDetailViewEvery(ListCreateAPIView):

    serializer_class = BookSerializer
    lookup_field = ["id", "categories"]

    def get_queryset(self):
        return Book.objects.filter()







class CommentList(ListCreateAPIView):

    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Book.objects.filter()

class CommentListEvery(ListCreateAPIView):

    serializer_class = CommentSerializer


    def get_queryset(self):
        return Book.objects.filter()











