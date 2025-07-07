from django.urls import path
from .views import job_list, company_jobs, create_job, job_detail, edit_job, delete_job

app_name = 'jobs'

urlpatterns = [
    path('', job_list, name='job_list'),
    path('my/', company_jobs, name='company_jobs'),
    path('create/', create_job, name='create_job'),
    path('<int:pk>/', job_detail, name='job_detail'),
    path('<int:pk>/edit/', edit_job, name='edit_job'),
    path('<int:pk>/delete/', delete_job, name='delete_job'),

]
