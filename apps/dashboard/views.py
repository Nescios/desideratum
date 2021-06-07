# Import Python

from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta

# Import Django

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# Import models

from apps.project.models import Entry, Project

# Import utilities

from .utilities import get_time_for_user_and_date, get_time_for_team_and_month, get_time_for_user_and_month, get_time_for_user_and_project_and_month, get_time_for_user_and_team_month

# Views

@login_required
def dashboard(request):
    
    # Get team and set variable

    all_projects = Project.objects.all()

    # User date, pagination

    num_days = int(request.GET.get('num_days', 0))
    date_user = datetime.now() - timedelta(days=num_days)

    date_entries = Entry.objects.filter(created_at__date=date_user, is_tracked=True)
    
    # User month, pagination

    user_num_months = int(request.GET.get('user_num_months', 0))
    user_month = datetime.now()-relativedelta(months=user_num_months)

    for project in all_projects:
        project.time_for_user_and_project_and_month = get_time_for_user_and_project_and_month(project, request.user, user_month)
    

    untracked_entries = Entry.objects.filter(is_tracked=False).order_by('-created_at')

    for untracked_entry in untracked_entries:
        untracked_entry.minutes_since = int((datetime.now(timezone.utc) - untracked_entry.created_at).total_seconds() / 60)

    # Context

    context = {
        'all_projects': all_projects,
        'projects': all_projects[0:4],
        'date_entries': date_entries,
        'num_days': num_days,
        'date_user': date_user,
        'untracked_entries': untracked_entries,
        'user_num_months': user_num_months,
        'user_month': user_month,
        'time_for_user_and_month': get_time_for_user_and_month(request.user, user_month),
        'time_for_user_and_date': get_time_for_user_and_date(request.user, date_user),
    }

    return render(request, 'dashboard/dashboard.html', context)

@login_required
def view_user(request, user_id):
    # Get team, user and set variables

    all_projects = Project.objects.all()

    # User date, pagination

    num_days = int(request.GET.get('num_days', 0))
    date_user = datetime.now() - timedelta(days=num_days)

    date_entries = Entry.objects.filter(created_at__date=date_user, is_tracked=True)
    
    # User month, pagination

    user_num_months = int(request.GET.get('user_num_months', 0))
    user_month = datetime.now()-relativedelta(months=user_num_months)

    for project in all_projects:
        project.time_for_user_and_project_and_month = get_time_for_user_and_project_and_month(project, request.user, user_month)

    # Context

    context = {
        'all_projects': all_projects,
        'date_entries': date_entries,
        'num_days': num_days,
        'date_user': date_user,
        'user_num_months': user_num_months,
        'user_month': user_month,
        'time_for_user_and_month': get_time_for_user_and_month(request.user, user_month),
        'time_for_user_and_date': get_time_for_user_and_date(request.user, date_user),
    }

    return render(request, 'dashboard/view_user.html', context)