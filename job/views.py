from django.shortcuts import render
from .models import Job 
from django.core.paginator import Paginator
from .form import ApplyForm
# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 1) 
    page_number = request.GET.get('page')
    job_list = paginator.get_page(page_number)
    context={'job_list': job_list}
    return render(request, 'job/job_list.html', context)

def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            apply = form.save(commit=False)
            apply.job = job_detail
            apply.save()
            print('Done')
    else:
        form = ApplyForm()  
        
    context ={'job': job_detail,
            'form': form,}
    return render(request, 'job/job_detail.html', context)