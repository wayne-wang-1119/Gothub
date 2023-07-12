import json

from braces.views import CsrfExemptMixin

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.views.generic import View
from github import Github

from .tasks import process_webhook


@csrf_exempt
def github_payload(request):
    if request.method == "POST":
        process_webhook(request.body)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def home(request):
    return render(request, "webhook_process/home.html")
