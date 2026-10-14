from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

import logging
import json

# from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Login view
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']

    user = authenticate(username=username, password=password)
    data = {"userName": username}

    if user is not None:
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}

    return JsonResponse(data)


# Logout view
@csrf_exempt
def logout_request(request):
    logout(request)
    data = {"userName": ""}
    return JsonResponse(data)


# Registration view
@csrf_exempt
def registration(request):
    # Load JSON data from the request body
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']

    username_exist = False

    try:
        # Check whether the username already exists
        User.objects.get(username=username)
        username_exist = True
    except User.DoesNotExist:
        logger.debug("%s is a new user", username)

    # Register and log in a new user
    if not username_exist:
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email
        )

        login(request, user)

        data = {
            "userName": username,
            "status": "Authenticated"
        }
        return JsonResponse(data)

    # Username already exists
    data = {
        "userName": username,
        "error": "Already Registered"
    }
    return JsonResponse(data)


# Get dealerships view
# def get_dealerships(request):
#     ...


# Get dealer reviews view
# def get_dealer_reviews(request, dealer_id):
#     ...


# Get dealer details view
# def get_dealer_details(request, dealer_id):
#     ...


# Add a review view
# def add_review(request):
#     ...
