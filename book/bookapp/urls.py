from django.urls import path
from .views import BookList, BookDetailView, BookListEvery, BookDetailViewEvery, CommentList, CommentListEvery, BookListCategory, BookListEveryCategory, BookPost, BookArchived


urlpatterns = [
    path('<is_archived>', BookListEvery.as_view(), name='home'),
    path('user/book/?<is_archived>/<int:id>', BookDetailView.as_view()),
    path('user/book/post', BookPost.as_view()),
    path('user/?<is_archived>', BookList.as_view()),
    path('user/?<is_archived>&<categories>', BookListCategory.as_view()),
    path('book/?<is_archived>/<int:id>', BookDetailViewEvery.as_view()),
    path('book/?<is_archived>&<categories>', BookListEveryCategory.as_view()),
    path('user/book/?<is_archived>/book/<int:id>/comment', CommentList.as_view()),
    path('book/?<is_archived>/book/<int:id>/comment', CommentListEvery.as_view()),
    path('user/book/<int:id>/archive', BookArchived.as_view()),
]