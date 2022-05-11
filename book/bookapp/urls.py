from django.urls import path
from .views import BookList, BookDetailView, BookListEvery, BookDetailViewEvery, CommentList, CommentListEvery, BookListCategory, BookListEveryCategory, BookPost, BookArchived, CategoryList,CategoryDetail,CategoryPost


urlpatterns = [
    path('archived/', BookListEvery.as_view(), name='home'),
    path('archived/<int:id>', BookDetailView.as_view()),
    path('post', BookPost.as_view()),
    path('archived/', BookList.as_view()),
    path('search-book/', BookListCategory.as_view()),
    path('archived/<int:id>', BookDetailViewEvery.as_view()),
    path('search-book/', BookListEveryCategory.as_view()),
    path('post/comment', CommentList.as_view()),
    path('comments', CommentListEvery.as_view()),
    path('<int:id>/archive', BookArchived.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
    path('categories/post', CategoryPost.as_view()),
]