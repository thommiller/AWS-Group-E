from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login, get_user
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from citations.models import Citation
from .forms import CitationForm


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



def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def citations(request):
    form = CitationForm()
    query_results = Citation.objects.filter(user=request.user)
    return render(request, 'citations.html', {'query_results': query_results, "form" : form})

@login_required
def citations_data(request):
    if request.method == "POST":
        form = CitationForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
        return redirect('/citations')
    else:
        form = CitationForm()


def deleteEntry(request, id):
    print("work")
    thingy = Citation.objects.get(pk = id)
    thingy.delete()
    return redirect('/citations')


