from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST','DELETE']) # or http_method_names = ['get']    
def home (request)-> Response:
    if request.method == 'GET':
         return Response({
        'message': 'Hello World!',
        'status':200,
        'method':'GET'
        })
    if request.method == 'POST':
         return Response({
        'message': 'Hello World!',
        'status':200,
        'method':'POST'
        })
    if request.method == 'PUT':
            return Response({
            'message': 'Hello World!',
            'status':200,
            'method':'PUT'
            })
    if request.method == 'DELETE':
            return Response({
            'message': 'Hello World!',
         'status':200,
            'method':'DELETE'
            })
    else :
          return Response({
        'message': 'Hello World!',
        'status':405,
        'method':'Method Not Allowed'
          })
    
'''
you can use @api_view method to define the methods that you want to use in your view

'''

# Compare this snippet from API/apps.py:
   