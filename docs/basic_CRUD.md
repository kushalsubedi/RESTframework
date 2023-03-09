## CRUD OPERATION
**what is CRUD ?**
-  CRUD is an acronym for Create, Read, Update and Delete. These are the four basic functions of persistent storage. Any application that uses a database will have to implement these functions at some point. In this tutorial, we will learn how to implement CRUD operations using Django REST framework.

**Create**
CRUD Operations with Function-Based Views

Function-based views (FBV) are a simpler way of defining views in Django. They are easy to understand and implement, making them a good choice for small projects or when you need to quickly prototype a new feature. Let's see how we can use FBVs to perform CRUD operations in DRF.

**Create Operation**

- The create operation is used to add a new object to the database. In DRF, we can create a new object by sending a POST request to the API endpoint. Here's how we can implement the create operation using FBVs:

```python
@api_view(['POST'])
def create_object(request):
    serializer = MyModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
```

- In the above code, we use the `@api_view` decorator to specify that this function-based view can only be accessed via a POST request. We then create a new instance of the MyModelSerializer class, passing in the request.data as the data to be serialized. We then check if the serializer is valid, and if it is, we save the serializer and return the serialized data with a status code of 201. If the serializer is not valid, we return the validation errors with a status code of 400.

**Read Operation**
- The read operation is used to retrieve objects from the database. In DRF, we can retrieve objects by sending a GET request to the API endpoint. Here's how we can implement the read operation using FBVs:

```python
@api_view(['GET'])
def get_object(request, pk):
    try:
        obj = MyModel.objects.get(pk=pk)
    except MyModel.DoesNotExist:
        return Response(status=404)
    
    serializer = MyModelSerializer(obj)
    return Response(serializer.data)
```
- In the above code, we use the `@api_view` decorator to specify that this function-based view can only be accessed via a `GET` request. We then use a `try-except` block to retrieve the object with the specified primary key `(pk)`. If the object does not exist, we return a `404 status code`. If the object exists, we create a new instance of the `My ModelSerializer` class, passing in the retrieved object as the data to be serialized. We then return the serialized data.

**Update Operation**

- The update operation is used to modify an existing object in the database. In DRF, we can update an object by sending a PUT or PATCH request to the API endpoint. Here's how we can implement the update operation using FBVs:

```python
@api_view(['PUT', 'PATCH'])
def update_object(request, pk):
    try:
        obj = MyModel.objects.get(pk=pk)
    except MyModel.DoesNotExist:
        return Response(status=404)
    
    serializer = MyModelSerializer(obj, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

```

- In the above code, we use the @api_view decorator to specify that this function-based view can only be accessed via PUT or PATCH request. We then use a try-except block to retrieve the object with the specified primary key (pk). If the object does not exist, we return a 404 status code. If the object exists, we create a new instance of the MyModelSerializer class, passing in the retrieved object as the instance to be updated and the request.data as the data to be serialized. We then check if the serializer is valid, and if it is, we save the serializer and return the serialized data. If the serializer is not valid, we return the validation errors with a status code of 400.
for demo code [click here](../API/views.py)

for more information visit [here](https://www.django-rest-framework.org/tutorial/quickstart/)



