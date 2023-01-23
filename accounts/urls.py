from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.views import TokenVerifyView
from accounts import views

urlpatterns = [
    path('login/', views.LoginApiView.as_view()),
    path('signup/', views.SignUpAPIView.as_view()),
    # 토큰
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]