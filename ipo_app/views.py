from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import IPODetails, User
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
from django.http import JsonResponse
import re
import json


def dashboard(request):
    return render(request, "ipo_app/dashboard.html")  # Ensure the path to your template is correct

def manage_ipo(request):
    return render(request, "ipo_app/manage_ipo.html")  # Ensure the path to your template is correct


def register_ipo(request):
    return render(request, "ipo_app/register_ipo.html")  # Ensure the path to your template is correct

@csrf_exempt
def create_account(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            if not username or not email or not password:
                return JsonResponse({'error': 'All fields are required'}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exists'}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email already exists'}, status=400)

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            return JsonResponse({'message': 'Account created successfully'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return render(request, 'ipo_app/signup.html')
    
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                return JsonResponse({'error': 'Username and password are required'}, status=400)

            # Check if the user exists in the database
            if not User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'User does not exist'}, status=404)

            # Authenticate user
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)  # Logs in the user
                return JsonResponse({'message': 'Login successful'}, status=200)
            else:
                return JsonResponse({'error': 'Invalid username or password'}, status=401)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return render(request, 'ipo_app/Login.html')




@csrf_exempt
def forgot_password(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')

            if not email:
                return JsonResponse({'error': 'Email is required'}, status=400)

            user = User.objects.filter(email=email).first()
            if not user:
                return JsonResponse({'error': 'No account associated with this email'}, status=404)

            temp_password = get_random_string(8)  # Generate random password
            user.set_password(temp_password)
            user.save()

            # Sending email (use your actual email configuration in settings.py)
            send_mail(
                'Password Reset',
                f'Your temporary password is: {temp_password}',
                'your_email@example.com',  # Replace with your email
                [email],
                fail_silently=False,
            )

            return JsonResponse({'message': 'Temporary password sent to your email'}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:

        return render(request, 'ipo_app/forgot-password.html')
