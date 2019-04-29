from django.urls import path
from . import views
from .views import BookDetailView, BookListView, load_servants

app_name = 'user'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('member_reg/', views.memreg_view, name='mem_reg'),
    path('member_list/', views.member_list_view, name='mem_list'),
    path('bookdetail/', views.book_detail_view, name='bookdetail'),
    path('check/', views.check_view, name='cehck'),

    path('maintain/', views.maintain_view, name='maintain'),
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('servant_request/', views.servant_request_view, name='servant_request'),
    path('ajax/load-servants/', views.load_servants, name='ajax_load_servants'),
    path('ajax/load_language/', views.load_lang, name='ajax_load_language'),


]