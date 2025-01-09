from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('company/', views.company_registration, name='company_registration'),
    path('create/', views.create_job, name='create_job'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/', views.job_list, name='job_post_form'),
    path('update/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete/<int:job_id>/', views.delete_job, name='delete_job'),
]
