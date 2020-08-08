from django.shortcuts import render
from .models import Course, Project, Session

# Create your views here.
def landing(request):
  courses = Course.objects.all()
  projects = Project.objects.all()
  sessions = Session.objects.all()

  return render(request, 'home/landing.html', {
    'courses': courses, 
    'projects': projects, 
    'sessions': sessions
  })