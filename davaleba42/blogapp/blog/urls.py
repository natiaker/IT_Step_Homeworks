from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='homepage'),
    path('post_details/<int:pk>', views.PostDetailsView.as_view(), name='post_details'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('remove_post/<int:pk>', views.RemovePostView.as_view(), name='remove_post'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
]

