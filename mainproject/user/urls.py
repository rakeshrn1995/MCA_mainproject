from django.urls import path
from . import views
from .views import BookListView, BookDetailView, load_servants

app_name = 'user'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('member_reg/', views.memreg_view, name='mem_reg'),
    path('bookdetail/', views.book_detail_view, name='bookdetail'),
    path('check/', views.check_view, name='cehck'),
    path('profile_update/', views.profile_view, name='profile_update'),
    path('maintain/', views.maintain_view, name='maintain'),
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('servant_request/', views.servant_request_view, name='servant_request'),
    path('ajax/load-servants/', views.load_servants, name='ajax_load_servants'),


]