from django.urls import path
from .views import home, about, projects

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('projects/', projects, name='project'),
]
