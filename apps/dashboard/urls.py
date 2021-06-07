# Import Django

from django.urls import path, include

# Import Views

from .views import dashboard, view_user

#

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('<int:user_id>/', view_user, name='view_user'),
    path('projects/', include('apps.project.urls')),
]