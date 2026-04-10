from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .forms import UserRegisterForm, ClimaticDataForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, is_admin=False)
            login(request, user)
            return redirect('user_dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def user_dashboard(request):
    return render(request, 'mainapp/user_dashboard.html')

@login_required
def climatic_data(request):
    if request.method == 'POST':
        form = ClimaticDataForm(request.POST)
        if form.is_valid():
            # Prediction logic placeholder
            prediction = "Suspicious"  # Replace with actual ML prediction
            return render(request, 'mainapp/prediction.html', {'prediction': prediction})
    else:
        form = ClimaticDataForm()
    return render(request, 'mainapp/prediction.html', {'form': form})

def is_admin(user):
    return hasattr(user, 'profile') and user.profile.is_admin

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    users = Profile.objects.filter(is_admin=False)
    return render(request, 'mainapp/admin_dashboard.html', {'users': users})

@login_required
@user_passes_test(is_admin)
def remove_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user.profile.is_admin:
        return redirect('admin_dashboard')
    user.delete()
    return redirect('admin_dashboard')
