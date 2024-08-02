# band/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import BandMember


def landing_page(request):
    return render(request, 'band/landing_page.html')

def members(request):
    return render(request, 'band/members.html')

def events(request):
    return render(request, 'band/events.html')

# band/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing_page')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# band/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def landing_page(request):
    return render(request, 'band/landing_page.html')

@login_required
def members(request):
    return render(request, 'band/members.html')

@login_required
def events(request):
    return render(request, 'band/events.html')

@login_required
def members(request):
    band_members = BandMember.objects.all()
    return render(request, 'band/members.html', {'band_members': band_members})