from django.urls import path

from .views import CampListView, NewsListView, NewsDetailView
from . import views


app_name = 'useradmin'

urlpatterns = [
    path('', views.adminhome_view, name='admin_home'),
    path('add_activity', views.addactivity_view, name='add_activity'),
    path('add_camp', views.addcamp_view, name='add_camp'),
    path('base/', views.test_view, name='base'),
    path('test/', views.sample_view, name='test'),
    path('servant_req/', views.ser_req_list, name='servant_req'),
    path('add_news/', views.add_news_view, name='add_news'),
    path('newslist/', NewsListView.as_view(), name='newslist'),
    path('newsdetail/<int:pk>/', NewsDetailView.as_view(), name='newsdetail'),
    path('camp_view', CampListView.as_view(), name='camp_view'),
    path('add_user', views.add_user_view, name='add_user'),
    path('servant_reg', views.signup_servant_view, name='servant_reg'),
    path('servant_list', views.servantlist_view, name='servant_list'),
    path('servant_list/<int:pk>', views.servantmanage_view, name='servant_detail'),
    path('accept/', views.acceptbtn_view, name='accept'),
    path('add_type/', views.maintaintype_view, name='add_type'),




]