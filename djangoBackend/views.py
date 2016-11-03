from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def login_data(request):
		print(request.POST)
		username= request.POST.get('email')
		password= request.POST.get('password')
		user = authenticate(username= username, password=password)
		if user is not None:
			print(user)
			return HttpResponseRedirect('citation')
		else:
			print("authentication failed")
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
		print('citations')
		if request.user.is_authenticated(): print('auth')
		return render(request, 'citations.html')

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')





