

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_view(request):
    return HttpResponse('Hello')

def goodbye_view(request):
    html = ('<http><body><h1>Goodbye</h1></body></html>')
    return HttpResponse(html)