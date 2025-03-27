from django.http import HttpResponse

def natal(request):
    return HttpResponse("<center><h1> Não é Natal</h1></center>")