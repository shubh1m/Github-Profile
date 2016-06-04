from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from Github.forms import SearchForm
import urllib.request
import requests
import collections

def index(request):
    BASE_URL = 'https://api.github.com/users/'
    form = SearchForm(request.POST or None)
    name = ''
    details = ''
    status = ''
    photo = ''

    if request.method == 'POST':
        try:
            name = request.POST.get('search')

            #print(request.POST)
            url = BASE_URL + name
            r = requests.get(url)
            print(r.status_code)
            if(r.status_code == 404):
                status = 'User "' + name + '" does not exists.'
            elif(r.status_code == 200):
                details = r.json()
                photo = details['avatar_url']
                name = details['login']

                details = (('Name', details['name']),
                            ('Bio', details['bio']),
                            ('UserID', details['login']),
                            ('Email', details['email']),
                            ('Company', details['company']),
                            ('Blog' , details['blog']),
                            ('Location' , details['location']),
                            ('Hireable' , details['hireable']),
                            ('Public Repos' , details['public_repos']),
                            ('Public Gists' , details['public_gists']),
                            ('Followers' , details['followers']),
                            ('Following' , details['following']),
                        )

                details = collections.OrderedDict(details)
            else:
                status = 'There is some error with your request. Please try again later.'
        
        except ConnectionError:
            status = "Connection Error!! Try again later"
        #except HTTPError:
        #    status = "Invalid HTTP Response!! Try again later"
        except:
            status = 'Error!! Try again later'

    context = {
        'form': form ,
        'name': name ,
        'status': status,
        'details': details,
        'photo': photo,
    }
    return render(request, 'index.html', context)
    
    '''data['Name'] = details.name
                data['Bio'] = details.bio
                data['UserID'] = details.login
                data['Email'] = details.email
                data['Company'] = details.company
                data['Blog'] = details.blog
                data['Location'] = details.location
                data['Hireable'] = details.hireable
                data['Public Repos'] = details.public_repos
                data['Public Gists'] = details.public_gists
                data['Followers'] = details.followers
                data['Following'] = details.following

                data = {
                    'Name' : details['name'],
                    'Bio' : details['bio'],
                    'UserID' : details['login'],
                    'Email' : details['email'],
                    'Company' : details['company'],
                    'Blog' : details['blog'],
                    'Location' : details['location'],
                    'Hireable' : details['hireable'],
                    'Public Repos' : details['public_repos'],
                    'Public Gists' : details['public_gists'],
                    'Followers' : details['followers'],
                    'Following' : details['following'],
                }


                    (('Name', data['name']),
                        ('Bio', data['bio']),
                        ('UserID', data['login']),
                        ('Email', data['email']),
                        ('Company', data['company']),
                        ('Blog' , data['blog'],
                        ('Location' , data['location'],
                        ('Hireable' , data['hireable'],
                        ('Public Repos' , data['public_repos'],
                        ('Public Gists' , data['public_gists'],
                        ('Followers' , data['followers'],
                        ('Following' , data['following'],
                        )
    '''