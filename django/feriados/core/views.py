from django.shortcuts import render

def natal(requests):
    contexto = {'natal': False, 'carnaval':False}
    # Fazendo uso do debugger
    # import ipdb; ipdb.set_trace()
    return render(requests, "natal.html", contexto)