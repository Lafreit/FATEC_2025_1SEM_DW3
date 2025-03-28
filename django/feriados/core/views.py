from django.shortcuts import render

def natal(requests):
    contexto = {'natal': False, 'carnaval':False}
    return render(requests, "natal.html", contexto)