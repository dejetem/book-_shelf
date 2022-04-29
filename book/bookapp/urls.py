from django.urls import path
from .views import BookList, BookDetailView, BookListEvery, BookDetailViewEvery, CommentList, CommentListEvery


urlpatterns = [
    path('', BookListEvery.as_view()),
    path('user/book/<int:id>', BookDetailView.as_view()),
    path('user/book/<int:id>', BookDetailView.as_view()),
    path('user/', BookList.as_view()),
    path('book/<int:id>', BookDetailViewEvery.as_view()),
    path('book/<int:id>', BookDetailViewEvery.as_view()),
]