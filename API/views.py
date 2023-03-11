from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
# # Create your views here.

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

@api_view(['PATCH'])
def update(request)->Response:
      try:
            data = request.data
            if not data.get('uid'):
                  return Response({
                        'status':False,
                        'message':'uid required',
                        'data':{}
                  })

            obj=Todo.objects.get(uid=data.get('uid'))
            serializer = TodoSerializer(obj,data=data,partial=True)
            if serializer.is_valid():
                  serializer.save()

                  return Response({
                        'status':True,
                        'message':'Succes data',
                        'data':serializer.data
                  })

      except Exception as e:
            print (e)
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
      
class Todo_view(APIView):
      def get(self,request)->Response:
            qs=Todo.objects.all()
            serializer = TodoSerializer(qs,many=True)
            return Response({ 
                  'status':200,
                  'message':'data fetched successfully',
                  'data':(serializer.data)
            }) 
      def post(self,request)->Response:
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
      def put(self,request,pk)->Response:
          
            try:
                  obj = self.get_object(pk)
                  data = request.data
                  serializer = TodoSerializer(obj,data=data)
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
            
 
      def delete(self,reques,pk)->Response:
            try:
                  obj=self.get_object(pk)
                  obj.delete()
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
                  
