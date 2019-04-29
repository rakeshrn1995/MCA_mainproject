from django.urls import path

from .views import CampListView
from . import views


app_name = 'useradmin'

urlpatterns = [
    path('', views.adminhome_view, name='admin_home'),
    path('add_activity', views.addactivity_view, name='add_activity'),
    path('add_camp', views.addcamp_view, name='add_camp'),
    path('base/', views.test_view, name='base'),
    path('test/', views.sample_view, name='test'),
    path('camp_view', CampListView.as_view(), name='camp_view'),



]