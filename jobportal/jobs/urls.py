from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile', views.profile, name='profile'),
    path('company_registration/', views.company_registration, name='company_registration'),
    path('create_job/', views.create_job, name='create_job'),
    path('job_list/', views.job_list, name='job_list'),
    path('job_post_form', views.create_job, name='job_post_form'),
    path('edit_job/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),
]
