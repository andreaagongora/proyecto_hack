from django.shortcuts import render
from django.http import HttpResponse

#def busqueda_productos(request):
#
#    return render(request, "index.html")


#def buscar(request):
#    mensaje = " Formulario enviado %r"%request.GET["exp"]
#
#    return HttpResponse(mensaje)


import requests

#def my_django_view(request):
#    if request.method == 'POST':
#        r = requests.post('https://api-hack.herokuapp.com/api/', params=request.POST)
#    else:
#        r = requests.get('https://api-hack.herokuapp.com/api/1', params=request.GET)
#    if r.status_code == 200:
#        return HttpResponse('Yay, it worked')
#    return HttpResponse('Could not save data')

import simplejson as json

def busqueda_productos(request):
    
    if request.method == 'POST':

        final= {'experiences':exp,'education':edu, 'addres':adre, 'email':email}
        json.dumps(final)
        rj =  json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
        r = requests.post('https://api-hack.herokuapp.com/api/', params=rj.POST)
        
    #return HttpResponse('Could not save data')

    return render(request, "index.html")

def buscar(request):
    r = requests.get('https://api-hack.herokuapp.com/api/2', params=request.GET)

    return HttpResponse(r)