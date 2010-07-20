from django.http import HttpResponse

def test1k(request):
    a = 'a'*1024
    return HttpResponse(a)

def test10k(request):
    a = 'a'*10240
    return HttpResponse(a)

def test1m(request):
    a = 'a'*1024*1024
    return HttpResponse(a)

