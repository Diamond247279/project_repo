from turtle import title
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Repo
from .forms import RepoForm
from django.contrib import messages
# Create your views here.
def homepage(request):
    repo=Repo.objects.all()
    context={
        'all_repo':repo
    }
    return render(request,'general/index.html',context)

def search(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    repo=Repo.objects.filter(project_title__icontains=q)
    context={
        'all_repo':search
    }
    return render(request,'general/search.html',context)


def insert(request):
    form=RepoForm(request.POST or None,request.FILES or None)
    context={
        'form':form
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request,'project submitted successfully')
            return redirect(reverse('index'))
        else:
            print(form.errors)
            messages.error(request,'unsuccessful')	
    return render(request,'general/insert.html',context)