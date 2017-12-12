from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    """index view"""
    context = {}
    context['project'] = Project.objects.all()
    context['text'] = Text.objects.all()
    return render(request, 'core/index.html', { 'context' : context })
