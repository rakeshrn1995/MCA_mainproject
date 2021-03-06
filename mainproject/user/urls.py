from django.urls import path
from . import views
from .views import *

app_name = 'user'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('member_reg/', views.memreg_view, name='mem_reg'),
    path('member_list/', views.member_list_view, name='mem_list'),
    path('bookdetail/', views.book_detail_view, name='bookdetail'),
    path('check/', views.check_view, name='check'),
    path('campview/', CampListView.as_view(), name='campview'),
    path('campdetail/<int:pk>/', CampDetailView.as_view(), name='campdetail'),
    path('profile/', views.profile_view, name='profile'),
    path('user_reg/', views.user_reg_view, name='user_reg'),
    path('maintain/', views.maintain_view, name='maintain'),
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('servant_request/', views.servant_request_view, name='servant_request'),
    path('ajax/load-servants/', views.load_servants, name='ajax_load_servants'),
    path('ajax/load_language/', views.load_lang, name='ajax_load_language'),
    path('payment/', views.payment_view, name='payment'),
    path('logout/', views.user_logout, name='logout'),
    path('newslist/', NewsListView.as_view(), name='newslist'),
    path('newsdetail/<int:pk>/', NewsDetailView.as_view(), name='newsdetail'),


]