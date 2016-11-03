from django.http import HttpResponseRedirect

def login_data(request):
        print(request.POST)
        return HttpResponseRedirect('/')