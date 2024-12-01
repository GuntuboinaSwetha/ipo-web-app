from django.shortcuts import render
from .models import IPODetails, User


def dashboard(request):
    return render(request, "ipo_app/dashboard.html")  # Ensure the path to your template is correct

def manage_ipo(request):
    return render(request, "ipo_app/manage_ipo.html")  # Ensure the path to your template is correct


def register_ipo(request):
    return render(request, "ipo_app/register_ipo.html")  # Ensure the path to your template is correct