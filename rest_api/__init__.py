from django.shortcuts import render, redirect
from .forms import IPOForm

def ipo_registration(request):
    if request.method == 'POST':
        form = IPOForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = IPOForm()
    return render(request, 'ipo_registration.html', {'form': form})
