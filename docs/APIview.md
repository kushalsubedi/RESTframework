## before starting 
- must start your app in development server
```zsh
python manage.py runserver
```

## @api_view decorator
@api_view decorator is used to convert function based views into API views. It takes a list of HTTP methods that the view should respond to as its only argument. If the incoming request doesn't match one of the specified methods, a 405 Method Not Allowed response will be returned.
see [views.py /home](../API/views.py)

## Serializers 
seralizer are used to convert complex data such as querysets and model instances into native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

**deserialization** is the process of converting data from a format that is easy to store or transmit to a format that is easy to use.

**model serializer** is a shortcut for creating serializer classes:
- An automatically determined set of fields.
- Simple default implementations for the create() and update() methods.
