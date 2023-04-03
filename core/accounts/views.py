# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .tasks import sendEmail
import requests
from django.views.decorators.cache import cache_page

# Create your views here.


def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h2>Done!</h2>")


@cache_page(60)
def test(request):
    response = requests.get("https://test-cache.free.beeceptor.com")
    return JsonResponse(response.json())
