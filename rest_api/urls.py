# urls.py in ipo_app
from django.urls import path
from .views import IPODetailsListCreate, IPODetailsRetrieveUpdateDestroy
from . import views
#
urlpatterns = [
    path('ipo-details/', IPODetailsListCreate.as_view(), name='ipo-details-list-create'),
    path('ipo-details/<int:pk>/', IPODetailsRetrieveUpdateDestroy.as_view(), name='ipo-details-detail'),
    path("signup/", views.signup_api, name="signup_api"),  # API endpoint for signup
    path('login/', views.login_api, name='login_api'),  # API endpoint for login
    path('forgot-password/', views.forgot_password_api, name='forgot_password_api'),  # API for forgot password
    # You can add more API routes as needed
]

