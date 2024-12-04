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

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def dashboard(request):
    return render(request, "ipo_app/dashboard.html")  # Ensure the path to your template is correct

def manage_ipo(request):
    return render(request, "ipo_app/manage_ipo.html")  # Ensure the path to your template is correct


def register_ipo(request):
    return render(request, "ipo_app/register_ipo.html")  # Ensure the path to your template is correct

def sign_up(request):
    return render(request,"admin_app/signup.html")


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def sign_up(request):
    if request.method == "POST":
        # Extract form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if a user with the same email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('sign_up')

        # Create the user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

        # Show a success message
        messages.success(request, "Account created successfully! Please log in.")

        # Redirect to the login page
        return redirect('login_user')  # Ensure the 'login_user' URL pattern exists in your urls.py

    return render(request, "admin_app/signup.html")

#login_user 
def login_user(request):
    print("endpoint login hit")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print("method success")

        if email and password:
            user = authenticate(request, username=email, password=password)
            print("fields successful")
            if user:
                login(request, user)  # Ensure this is imported at the top: `from django.contrib.auth import login`
                print("login successful")
                return redirect('dashboard')  # Corrected template path for redirection after login
            else:
                messages.error(request, 'Invalid email or password')
                print("invalid credentials")
                return render(request, 'admin_app/login.html')  # Corrected template path for invalid login

        messages.error(request, 'Both fields are required')
        print("fields missing")
        return render(request, 'admin_app/login.html')  # Corrected template path for missing fields

    # If the request method is GET, render the login page
    return render(request, 'admin_app/login.html')  # Correct template path for GET request



'''@csrf_exempt
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

        return render(request, 'admin_app/forgot-password.html')'''
