from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
import urllib.request, json
import requests
from Github.forms import SearchForm

def index(request):
    BASE_URL = 'https://api.github.com/users/'
    form = SearchForm(request.POST or None)
    name = None
    details = None

    if request.method == 'POST':
        try:
            name = request.POST.get('search')

            #print(request.POST)
            url = BASE_URL + name
            r = requests.get(url)
            #print(r.status_code)
            #if(r.status_code == 200)
            details = r.json()
        except ConnectionError:
            print("Connection Error!! Try again later")
        except HTTPError:
            print("Invalid HTTP Response")
        except:
            print('Error in try block')

    context = {
        'form': form ,
        'name': name ,
        'details': details,
    }
    return render(request, 'index.html', context)
    