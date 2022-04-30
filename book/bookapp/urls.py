from django.urls import path
from .views import BookList, BookDetailView, BookListEvery, BookDetailViewEvery, CommentList, CommentListEvery, BookListCategory, BookListEveryCategory


urlpatterns = [
    path('', BookListEvery.as_view()),
    path('user/book/<int:id>', BookDetailView.as_view()),
    path('user/', BookList.as_view()),
    path('user/?categories:name', BookListCategory.as_view()),
    path('book/<int:id>', BookDetailViewEvery.as_view()),
    path('book/?categories:name', BookListEveryCategory.as_view()),
    path('user/book/<int:id>', CommentList.as_view()),
    path('book/<int:id>', CommentListEvery.as_view()),
]