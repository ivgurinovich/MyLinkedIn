from django.urls import path
from .views import (
    resume_create,
    resume_list,
    resume_view,
    resume_edit,
    resume_detail,
    delete_resume,
    apply_to_job,
    job_applications,
)

app_name = 'resumes'

urlpatterns = [
    path('', resume_list, name='resume_list'),
    path('create/', resume_create, name='resume_create'),
    path('me/', resume_view, name='resume_view'),
    path('<int:pk>/edit/', resume_edit, name='resume_edit'),
    path('<int:pk>/', resume_detail, name='resume_detail'),
    path('<int:pk>/delete/', delete_resume, name='delete_resume'),
    path('apply/<int:job_id>/', apply_to_job, name='apply'),
    path('job/<int:pk>/applications/', job_applications, name='job_applications'),
]
