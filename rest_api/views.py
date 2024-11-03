# api.py in rest_api

from rest_framework import generics
from ipo_app.models import IPODetails  # Import the model from ipo_app
from .serializers import IPODetailsSerializer

# List and create IPO details
class IPODetailsListCreate(generics.ListCreateAPIView):
    queryset = IPODetails.objects.all()
    serializer_class = IPODetailsSerializer

# Retrieve, update, and delete an IPO detail
class IPODetailsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPODetails.objects.all()
    serializer_class = IPODetailsSerializer
