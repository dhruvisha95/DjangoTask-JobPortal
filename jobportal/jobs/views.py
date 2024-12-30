from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.paginator import Paginator

from django.shortcuts import render, redirect
from .forms import CompanyRegistrationForm
from django.contrib.auth.decorators import login_required

from .forms import JobPostForm
from .models import JobPost

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('company_registration')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('company_registration')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def company_registration(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            return redirect('job_list')
    else:
        form = CompanyRegistrationForm()
    return render(request, 'company_registration.html', {'form': form})

@login_required
def create_job(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user.company
            job.save()
            return redirect('job_list')
    else:
        form = JobPostForm()
    return render(request, 'job_post_form.html', {'form': form})

@login_required
def job_list(request):
    jobs = JobPost.objects.filter(company=request.user.company)
    paginator = Paginator(jobs, 5)  # Show 5 jobs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'job_list.html', {'jobs': page_obj})


@login_required
def edit_job(request, job_id):
    job = JobPost.objects.get(id=job_id)
    if job.company.user != request.user:
        return redirect('job_list')
    if request.method == 'POST':
        form = JobPostForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobPostForm(instance=job)
    return render(request, 'job_post_form.html', {'form': form})

@login_required
def delete_job(request, job_id):
    job = JobPost.objects.get(id=job_id)
    if job.company.user == request.user:
        job.delete()
    return redirect('job_list')

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

