from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login, get_user
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from citations.models import Citation

def login_data(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/citations', permanent=True) #the / in front of citations is important, so it is a hardcoded url
        else:
            print("authentication failed")
            return redirect('/')        

def registration_data(request):
        username= request.POST.get('username')
        password= request.POST.get('password')
        email= request.POST.get('email')
        firstname= request.POST.get('first_name')
        lastname= request.POST.get('last_name')

        user = User.objects.create_user(username, email, password, first_name=firstname, last_name=lastname)
        return redirect('/')

@login_required
def citations_data(request):
    if request.method == "POST":
        author_fname = request.POST.get("author_fname")
        author_lname = request.POST.get("author_lname")
        title = request.POST.get("title")
        link = request.POST.get("url")
        date_acc = request.POST.get("date_acc")
        date_pub = request.POST.get("date_pub")
        notes = request.POST.get("notes")
        a_citation = Citation(author_fname=author_fname, author_lname=author_lname, title=title, link=link, date_acc=date_acc, date_pub=date_pub, notes=notes)
        a_citation.user = get_user(request)
        a_citation.save(force_insert=True)
    return redirect('/citations')

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def citations(request):
    query_results = Citation.objects.filter(user=request.user)
    return render(request, 'citations.html', {'query_results': query_results})
