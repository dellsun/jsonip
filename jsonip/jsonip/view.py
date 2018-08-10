from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world ! ")


def jsonip(request):
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip =  request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    return HttpResponse(ip)