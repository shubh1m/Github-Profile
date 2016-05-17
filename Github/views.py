from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import urllib.request
from Github.forms import SearchForm

'''
def home(request):
    form = SearchForm()
    print('in home')
    return render(request, 'index.html', {'form': form})
'''

def index(request):
    url = 'https://api.github.com/users/'
    form = SearchForm(request.POST or None)
    name = ''

    if request.method == 'POST':
        name = request.POST.get('search')

    context = {
        'form': form ,
        'name': name ,
    }
    return render(request, 'index.html', context)

'''
def Search(request):
    url = 'https://api.github.com/users/'

    if request.method == 'POST':
        name = request.POST.get('search')
        return HttpResponse('thanks')
        #return render_to_response('Github/index.html', {'name': name}, RequestContext(request))
        #return render(request, 'Github/index.html', {'name': name})
    else:
        form = SearchForm()
    return render(request, 'index.html', {'form': form, 'name': name})
'''