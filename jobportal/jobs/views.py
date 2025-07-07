from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from .forms import JobForm


def job_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    jobs = Job.objects.filter(is_active=True)
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def company_jobs(request):
    if not request.user.is_authenticated or request.user.role != 'company':
        return redirect('accounts:login')
    jobs = Job.objects.filter(company=request.user)
    return render(request, 'jobs/company_jobs.html', {'jobs': jobs})


def create_job(request):
    if not request.user.is_authenticated or request.user.role != 'company':
        return redirect('login')

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user
            print(f"[DEBUG] Job will be created by: {request.user} with role: {request.user.role}")
            job.save()
            print(f"[DEBUG] Job saved! Title: {job.title}, ID: {job.id}")
            return redirect('jobs:company_jobs')
    else:
        form = JobForm()

    return render(request, 'jobs/create_job.html', {'form': form})


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})


def delete_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    print("[DEBUG] Viewing job:", job)
    if request.user == job.company:
        job.delete()

    return redirect('jobs:company_jobs')


def edit_job(request, pk):
    job = Job.objects.get(pk=pk)
    print("[DEBUG] Editing job:", job)
    form = JobForm(request.POST or None, instance=job)
    if form.is_valid():
        form.save()
        return redirect('jobs:company_jobs')

    return render(request, 'jobs/edit_job.html', {'form': form})
