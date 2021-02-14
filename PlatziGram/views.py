"""Platzigram views"""

# Django
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import JsonResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server is {now}'.format(now=str(now)))


def sorted(request):
    """Hi."""
    #import pdb; pdb.set_trace()
    numbers = [int(i) for i in request.GET['numbers'].split(",")]
    sorted_numbers = sorted(numbers)
    #response = JsonResponse(sorted(numbers), safe=False)
    data = {
        'status' : 'ok',
        'numbers' : sorted_numbers,
        'message' : 'Integers sorted succesfully'
    }
    return HttpResponse(json.dumps(data, indent=4) , content_type='application/json')
    #return JsonResponse(data)

def say_hi(request, name, age):
    """Say Hi! """
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to PlatziGram'.format(name)

    return HttpResponse(message)