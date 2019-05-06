from django.urls import path
from . import views


app_name = 'manager'

urlpatterns = [
    path('', views.home_view, name='manager_home'),
    path('servant_reg', views.signup_servant_view, name='servant_reg'),
    path('servant_list', views.servantlist_view, name='servant_list'),
    path('servant_list/<int:pk>', views.servantmanage_view, name='servant_detail'),

]
