from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume, Application
from .forms import ResumeForm, ApplicationForm
from jobs.models import Job


def resume_create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('resumes:resume_list')
    else:
        form = ResumeForm()

    return render(request, 'resumes/resume.html', {'form': form})


def resume_list(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'resumes/resume_list.html', {'resumes': resumes})


def resume_view(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    resume, created = Resume.objects.get_or_create(user=request.user)
    if not created:
        return redirect('resumes:resume_edit', pk=resume.pk)

    return redirect('resumes:resume_edit', pk=resume.pk)


def resume_edit(request, pk):
    resume = get_object_or_404(Resume, pk=pk)

    if request.user != resume.user:
        return redirect('resumes:resume_list')

    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('resumes:resume_list')
    else:
        form = ResumeForm(instance=resume)

    return render(request, 'resumes/resume.html', {'form': form, 'resume': resume})


def delete_resume(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    if request.user == resume.user:
        resume.delete()
    return redirect('resumes:resume_list')


def apply_to_job(request, job_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    job = get_object_or_404(Job, pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.applicant = request.user
            app.job = job
            app.save()
            return redirect('jobs:job_detail', pk=job.id)
    else:
        form = ApplicationForm()

    return render(request, 'resumes/apply.html', {'form': form, 'job': job})


def resume_detail(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'resumes/resume_detail.html', {'resume': resume})


def job_applications(request, pk):
    if not request.user.is_authenticated or request.user.role != 'company':
        return redirect('accounts:login')

    job = get_object_or_404(Job, pk=pk, company=request.user)
    applications = Application.objects.filter(job=job)

    return render(request, 'jobs/job_applications.html', {
        'job': job,
        'applications': applications
    })
