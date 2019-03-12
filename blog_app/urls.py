from django.urls import path
from blog_app.views import index, detail_content, login_view, logout_view, register_view
from django.contrib.auth import views

urlpatterns = [
    path('', index, name='home'),
    path('post/<int:pk>/', detail_content, name="detail-content"),
    path('login/', login_view, name="login-view"),
    path('logout/', logout_view, name="logout-view"),
    path('register/', register_view, name="register-view"),

]
