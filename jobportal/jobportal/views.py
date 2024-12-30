# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, logout
# from django.contrib import messages

from django.shortcuts import render, redirect
# from .forms import CompanyRegistrationForm
# from django.contrib.auth.decorators import login_required

# from .forms import JobPostForm
# from .models import JobPost

def home(request):
    return render(request, 'home.html')