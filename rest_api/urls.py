# urls.py in ipo_app
from django.urls import path
from .views import IPODetailsListCreate, IPODetailsRetrieveUpdateDestroy
#
urlpatterns = [
    path('ipo-details/', IPODetailsListCreate.as_view(), name='ipo-details-list-create'),
    path('ipo-details/<int:pk>/', IPODetailsRetrieveUpdateDestroy.as_view(), name='ipo-details-detail'),
]
