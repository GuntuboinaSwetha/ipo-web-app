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
    return render((request,"admin_app/signup.html"))


@csrf_exempt  # Remove this in production
def create_account(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            if not username or not email or not password:
                messages.error(request, 'All fields are required')
                return render(request, 'admin_app/signup.html')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return render(request, 'admin_app/signup.html')

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            messages.success(request, 'Account created successfully')
            return redirect('login_user')  # Redirect to the login page

        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return render(request, 'admin_app/signup.html')

    return render(request, 'admin_app/signup.html')



@csrf_exempt  # Remove this in production
def login_user(request):
    print("endpoint login hit")
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print("metho success")

        if email and password:
            user = authenticate(request, username=email, password=password)
            print("fileds succesfull")
            if user:
                login(request, user)  # Ensure this is imported at the top: `from django.contrib.auth import login`
                print("login")
                return render(request,"ipo_app/dashboard.html")
            else:
                messages.error(request, 'Invalid email or password')
                print("invslid")
                return render(request, 'admin_app/login.html')  # Correct template for login

        messages.error(request, 'Both fields are required')
        print("fields missing")
        return render(request, 'admin_app/login.html')  # Correct template for login

    # If the request method is GET, render the login page
    return render(request, 'admin_app/login.html')




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

        return render(request, 'admin_app/forgot-password.html')
