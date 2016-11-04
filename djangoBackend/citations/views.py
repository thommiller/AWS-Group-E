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
    return render(request, template_name = 'citations.html', context = {
        'query_results' : models.Citation.objects.all(),
        'obj': models.Citation.objects.all(),
    })
    
@login_required        
def citations_data(request):
    query_results = Citation.objects.all()
    if request.method == "POST":
        author = request.POST.get("author_fname") + " " + request.POST.get("author_lname")
        title = request.POST.get("title")
        link = request.POST.get("url")
        date_acc = request.POST.get("date_acc")
        date_pub = request.POST.get("date_pub")
        notes = request.POST.get("notes")
        a_citation = Citation(author=author, title=title, link=link, date_acc=date_acc, date_pub=date_pub, notes=notes, user = request.user)
        a_citation.save(force_insert=True)
    return HttpResponseRedirect('/citations')    
    
#def citations(request): #view to display all citations in db
#    return render(request, 'citations.html', {'obj': models.Citation.objects.all()})
