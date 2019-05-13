from django.urls import path

from login.views import *

from .views import *
from . import views

app_name = 'login'
urlpatterns = [
    path('login/', views.login_def, name='login'),
    path('home/', views.home_page, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('test/', views.test_view, name='test'),
    path('', views.index_view, name='homepage'),
    path('news/', NewsListView.as_view(), name='news'),
    path('newsdetail/<int:pk>/', NewsDetailView.as_view(), name='newsdetail'),
    path('mission/', views.mission_view, name='mission'),




]
