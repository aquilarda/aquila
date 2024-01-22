from django.shortcuts import render
from core.models import About, Project, Blog

def home(request):
    about = About.objects.all()
    project = Project.objects.all()
    context = {'about': about, 'project': project}
    return render(request, 'core/home.html', context)

def blog(request):
    blog = Blog.objects.all()
    context = {'blog': blog}
    return render(request, 'core/blog.html', context)
