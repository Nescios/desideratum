# Import Python
from datetime import datetime
# Import Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
# Import models
from .models import Project, Task, Entry


# Create your views here.

@login_required
def projects(request):
    projects = Project.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            project = Project.objects.create(title=title)

            messages.info(request, 'The project was added!')

            return redirect('project:projects')
    
    return render(request, 'project/index.html', {'projects': projects})