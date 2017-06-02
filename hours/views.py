from django.shortcuts import render

#Import JsonResponse to manage easier a JSON response
from django.http import JsonResponse

#Import datetime to get the ISO hour
import datetime


def hours_index(request):
	#Create a response with the index 'hora_actual' and the value with the actual hour
    responseData = {
        'hora_actual': datetime.datetime.now().isoformat()
    }

    return JsonResponse(responseData)