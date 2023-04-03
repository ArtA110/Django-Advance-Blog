# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .tasks import sendEmail
import requests
# Create your views here.


def send_email(request):
    sendEmail.delay()
    return HttpResponse('<h2>Done!</h2>')

def test(request):
    response = requests.get('https://test-cache.free.beeceptor.com')
    return JsonResponse(response.json())
