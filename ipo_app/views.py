from django.shortcuts import render
from .models import IPODetails, User


def dashboard(request):
    return render(request, "ipo_app/dashboard.html")  # Ensure the path to your template is correct

