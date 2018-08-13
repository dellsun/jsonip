from django.http import HttpResponse
import json
 
def hello(request):
    return HttpResponse("Hello world ! ")


def jsonip(request):
    result = {}

    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        result["ip"] =  request.META['HTTP_X_FORWARDED_FOR']
    else:
        result["ip"] = request.META['REMOTE_ADDR']

    return HttpResponse(json.dumps(result))