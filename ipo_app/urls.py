from django.urls import path
from . import views



urlpatterns = [
   
    path("dashboard/",views.dashboard,name="dashboard"),
    path("manage_ipo",views.manage_ipo,name="manage_ipo"),
    path("register_ipo",views.register_ipo,name="register_ipo"),
    #path("create_account",views.create_account,name='create_account'),
    path("login_user/",views.login_user,name="login_user"),

    path("sign_up/",views.sign_up,name="sign_up")
    
]