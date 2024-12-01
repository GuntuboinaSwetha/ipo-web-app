from django.urls import path
from . import views

urlpatterns = [
   
    path("dashboard/",views.dashboard,name="dashboard"),
    path("manage_ipo",views.manage_ipo,name="manage_ipo"),
    path("register_ipo",views.register_ipo,name="register_ipo"),
  
]