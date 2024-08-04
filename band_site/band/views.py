# band/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import BandMember

def landing_page(request):
    """
    Render the landing page for the band site.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response with the rendered landing page.
    """
    return render(request, 'band/landing_page.html')

@login_required
def members(request):
    """
    Render the members page with a list of band members.

    Requires user to be logged in.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response with the rendered members page,
        including a list of band members.
    """
    band_members = BandMember.objects.all()
    return render(request, 'band/members.html', {'band_members': band_members})

@login_required
def events(request):
    """
    Render the events page.

    Requires user to be logged in.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response with the rendered events page.
    """
    return render(request, 'band/events.html')

def register(request):
    """
    Handle user registration using the UserCreationForm.

    If the form is valid, the user is created and logged in automatically.
    Redirects to the landing page upon successful registration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response with the rendered registration page,
        or a redirect to the landing page after successful registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing_page')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
