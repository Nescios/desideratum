# Import Python

from datetime import datetime

# Models 

from apps.project.models import Entry

# Utility functions

def get_time_for_user_and_date(user, date):
    entries = Entry.objects.filter(created_at__date=date, is_tracked=True)

    return sum(entry.minutes for entry in entries)

def get_time_for_team_and_month(month):
    entries = Entry.objects.filter(created_at__year=month.year, created_at__month=month.month, is_tracked=True)

    return sum(entry.minutes for entry in entries)

def get_time_for_user_and_month(user, month):
    entries = Entry.objects.filter(created_at__year=month.year, created_at__month=month.month, is_tracked=True)

    return sum(entry.minutes for entry in entries)

def get_time_for_user_and_project_and_month(project, user, month):
    entries = Entry.objects.filter(project=project, created_at__year=month.year, created_at__month=month.month, is_tracked=True)

    return sum(entry.minutes for entry in entries)

def get_time_for_user_and_team_month(user, month):
    entries = Entry.objects.filter(created_by=user, created_at__year=month.year, created_at__month=month.month, is_tracked=True)

    return sum(entry.minutes for entry in entries)