from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def login_data(request):
		print(request.POST)
		username = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/citations')
		else:
			return HttpResponseRedirect('/')        

def registration_data(request):
        print(request.POST)
         
        username= request.POST.get('username')
        password= request.POST.get('password')
        email= request.POST.get('email')
        firstname= request.POST.get('first_name')
        lastname= request.POST.get('last_name')

        user = User.objects.create_user(username, email, password, first_name=firstname, last_name=lastname)
        return HttpResponseRedirect('/')

@login_required
def citations(request):
    return render(request, 'citations.html', {'obj': models.Citation.objects.all()})
# def citations(request):
		# print('citations')
		# if request.user.is_authenticated(): print('auth')
		# return render(request, 'citations.html')
        
@login_required        
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

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
