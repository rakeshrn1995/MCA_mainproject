from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login_def, name='login'),
    path('home/', views.home_page, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('member_reg/', views.memreg_view, name='mem_reg'),

]