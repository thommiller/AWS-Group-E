from django.http import HttpResponseRedirect
from django.db.models.loading import get_model
from citations.models import Citation


def login_data(request):
        print(request.POST)
        return HttpResponseRedirect('/')

def citations_data(request):
    query_results = Citation.objects.all()
    if request.method == "POST":
        author = request.POST.get("author_fname")
        title = request.POST.get("title")
        link = request.POST.get("url")
        date_acc = request.POST.get("date_acc")
        date_pub = request.POST.get("date_pub")
        notes = request.POST.get("notes")
        a_citation = Citation(author=author, title=title, link=link, date_acc=date_acc, date_pub=date_pub, notes=notes)
        a_citation.save(force_insert=True)
    return HttpResponseRedirect('/citations')

#def citation_data(request):
#        print(request.POST)
#        author = request.POST.get("author")
#        title = request.POST.get("title")
#        link = request.POST.get("link")
##        date_pub = request.POST.get("date_pub")
#        date_acc = request.POST.get("date_acc")
#        note = request.POST.get("note")
#        citation = Citation.objects.Create(author=author, title=title, link=link, date_pub=date_pub, date_acc=date_acc, note=note)
#        print(citation)
#        return HttpResponseRedirect('/')
