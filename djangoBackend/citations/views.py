from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from . import models
from .models import Citation
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders

# Create your views here.
def index(request):
    return render(request, template_name = "signup-page.html")

@login_required
def citations(request):
    return render(request, template_name = 'citations.html', context = {'obj': models.Citation.objects.all()})
#def citations(request): #view to display all citations in db
#    return render(request, 'citations.html', {'obj': models.Citation.objects.all()})
