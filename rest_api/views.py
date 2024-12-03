# api.py in rest_api

from rest_framework import generics
from ipo_app.models import IPODetails  # Import the model from ipo_app
from .serializers import IPODetailsSerializer
from django.http import JsonResponse

# List and create IPO details
class IPODetailsListCreate(generics.ListCreateAPIView):
    queryset = IPODetails.objects.all()
    serializer_class = IPODetailsSerializer

# Retrieve, update, and delete an IPO detail
class IPODetailsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPODetails.objects.all()
    serializer_class = IPODetailsSerializer




# def signup_api(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Logic to save user to the database
#         return JsonResponse({"message": "Account created successfully!"}, status=201)

#     return JsonResponse({"error": "Method not allowed"}, status=405)


    
# def login_api(request):
#     if request.method == "POST":
#         # Handle user login logic here (e.g., checking credentials)
#         return JsonResponse({"message": "Login successful!"}, status=200)
#     else:
#         return JsonResponse({"error": "Method not allowed"}, status=405)

# def forgot_password_api(request):
#     if request.method == "POST":
#         # Handle forgot password logic here (e.g., sending reset email)
#         return JsonResponse({"message": "Password reset link sent!"}, status=200)
#     else:
#         return JsonResponse({"error": "Method not allowed"}, status=405)       
