from django.urls import path
from . import views


urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register-user"),
    path('success', views.success, name="success"),
    path('verify/<str:auth_token>',views.verify, name="verify"),
    path('error', views.error_page, name="error"),
]