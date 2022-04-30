from django.urls import path
from .views import RegisterView, LoginView, LogoutAPIView
from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutAPIView.as_view(), name="logout"),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]