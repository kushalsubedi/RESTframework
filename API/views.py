from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
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
        'message': 'Hello POST',
        'status':200,
        'method':'POST'
        })
    if request.method == 'PUT':
            return Response({
            'message': 'Hello PUT',
            'status':200,
            'method':'PUT'
            })
    if request.method == 'DELETE':
            return Response({
            'message': 'Hello DELETE',
         'status':200,
            'method':'DELETE'
            })
    else :
          return Response({
        'message': 'Hello torilaurey',
        'status':405,
        'method':'Method Not Allowed'
          })
    
'''
you can use @api_view method to define the methods that you want to use in your view

'''
@api_view(['POST']) 
def create_todo(request)->Response:
        try:
            data = request.data
            serializer = TodoSerializer(data=data)
            print (data)
            if serializer.is_valid():
                  serializer.save()
                  print(serializer.data)
                  return Response({ 
                        'status':200,
                        'message':'Todo created successfully',
                        'data':serializer.data
                  })
        except Exception as e:
            return Response({
                  'status':500,
                  'message':str(e),
                  'data':{}
            })
@api_view(['GET']) 
def Listview(request)->Response:
      qs=Todo.objects.all()
      serializer = TodoSerializer(qs,many=True)
      return Response({ 
            'status':200,
            'message':'data fetched successfully',
            'data':(serializer.data)
      })    

@api_view(['PUT'])
def update(request,id)->Response:
   
      try:
            qs=Todo.objects.get(id=id)
            serializer = TodoSerializer(qs,data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response({ 
                        'status':200,
                        'message':'Todo updated successfully',
                        'data':serializer.data
                  })
      except Exception as e:
            return Response({
                  'status':500,
                  'message':str(e),
                  'data':{}
            })
@api_view(['DELETE'])
def delete(request,id)->Response:
      try:
            qs=Todo.objects.get(id=id)
            qs.delete()
            return Response({ 
                  'status':200,
                  'message':'Todo deleted successfully',
                  'data':{}
            })
      except Exception as e:
            return Response({
                  'status':500,
                  'message':str(e),
                  'data':{}
            })
      


      

# Compare this snippet from API/apps.py:
   