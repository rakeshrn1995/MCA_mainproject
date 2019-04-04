from django.urls import path
from . import views
from .views import ServantListView

app_name = 'manager'

urlpatterns = [
    # path('', views.home_view, name='manager_home'),
    path('servant_reg', views.signup_servant_view, name='servant_reg'),
    path('', ServantListView.as_view(), name='servant_view'),

]
