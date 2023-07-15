import datetime
import json
import os

import requests
from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from github import Github

from .tasks import process_webhook


@csrf_exempt
def github_payload(request: WSGIRequest):
    print(request)
    print(type(request))

    return HttpResponse(status=200)

    if request.method == "POST":
        payload = json.loads(request)
        username = payload["sender"]["login"]

        try:
            User = None
            user = User.objects.get(github_username=username)
            github_token = github_auth(user)

            # Pass the GitHub token to process_webhook
            process_webhook(request, github_token)
            return HttpResponse(status=200)
        except ObjectDoesNotExist:
            # User does not exist in our database, ask them to install GitHub App
            message = f"The user '{username}' has not installed the GitHub App."
            return HttpResponse(message, status=400)

    else:
        return HttpResponse(status=400)


def home(request):
    return render(request, "webhook_process/home.html")


def github_auth(user):
    # Check if the token has expired
    if user.token_expires_at <= datetime.datetime.now():
        # Token has expired, request a new one
        headers = {
            "Authorization": f'Bearer {os.getenv("GITHUB_APP_PRIVATE_KEY")}',
            "Accept": "application/vnd.github.v3+json",
        }
        response = requests.post(
            f"https://api.github.com/app/installations/{user.github_installation_id}/access_tokens",
            headers=headers,
        )
        if response.status_code == 201:
            # Successfully got a new token
            token_data = response.json()
            user.github_token = token_data["token"]
            user.token_expires_at = datetime.datetime.strptime(
                token_data["expires_at"], "%Y-%m-%dT%H:%M:%SZ"
            )
            user.save()

            # Request user details from GitHub to get the username
            headers = {
                "Authorization": f"Bearer {user.github_token}",
                "Accept": "application/vnd.github.v3+json",
            }
            response = requests.get(
                "https://api.github.com/user",
                headers=headers,
            )
            if response.status_code == 200:
                user_data = response.json()
                user.github_username = user_data["login"]
                user.save()

    return user.github_token


# def register_user(request):
#     if request.method == "GET":
#         code = request.GET.get("code")

#         if code is None:
#             return HttpResponseBadRequest("Error: No code provided.")

#         # Fetch the access token
#         access_token_url = "https://github.com/login/oauth/access_token"
#         headers = {"Accept": "application/json"}
#         data = {
#             "client_id": os.getenv("GITHUB_CLIENT_ID"),
#             "client_secret": os.getenv("GITHUB_CLIENT_SECRET"),
#             "code": code,
#         }
#         response = requests.post(access_token_url, headers=headers, data=data)

#         if response.status_code != 200:
#             return HttpResponseBadRequest("Error: Invalid code.")

#         access_token = response.json()["access_token"]

#         # Fetch the user's GitHub username
#         user_api_url = "https://api.github.com/user"
#         headers = {
#             "Authorization": f"Bearer {access_token}",
#             "Accept": "application/vnd.github.v3+json",
#         }
#         response = requests.get(user_api_url, headers=headers)

#         if response.status_code != 200:
#             return HttpResponseBadRequest("Error: Could not fetch user info.")

#         github_username = response.json()["login"]

#         # Check if the user already exists
#         user, created = User.objects.get_or_create(github_username=github_username)

#         # Update Database User Info
#         user.github_token = access_token
#         user.token_expires_at = timezone.now() + datetime.timedelta(
#             minutes=55
#         )  # expires after one hour of creation
#         user.save()

#         return HttpResponse("Login successful.")

#     else:
#         return HttpResponseBadRequest("Error: Invalid request method.")
