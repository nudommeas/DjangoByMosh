**What are Rest APIs?**
\\ API stands for Application Programming Interface \\ 
# Interface means a point where two different systems meet to communicate and exchange information, acting as a bridge for interaction.

--> Buiding an API is essentially building an interface that client apps can ues to get or save that data.
--> APis is going to have a bunch of endpoints for different purposes. So we can have an endpoint for getting a list of product /products as well as creating, updating , deleting them. 
--> We can hava other endpoints for managing our shopping cart /carts or orders /orders.
--> Client apps can request to the endpoints to get or save products,orders,shopping carts.

**Resources**
--> The resource in a RESTful API is like an object in the application, like product,collection,cart.
--> Client app can access them using a URL. URL stands for Uniform Recourse Locator.

**Resource Representation**
--> We can identify a resource using its URL
--> When the client app hits that URL, the server is going to return that resource in a certain format or representation.
--> It may return as JSON
--> On the server, we identify a resource like a product using an object,when we return back to the client, we're going to represent it as HTML, XML or JSON, because these are formats that client can understand.

# Important Note: A resource representation is the format (usually JSON) used to tranfer a resource between client and server.

# JSON stands for Javascript Object Notation
>> It's a lightweight data format used to send and receive data, especially in REST APIs.
--> In JSON, we represent an object using a pair of culy braces
--> Insie the braces, we can have a bunch of key-value pairs or properties.

**Installing Django REST Framework**
After the installation, include `rest_framework` to INSTALLED_APPS in the setting.py

**Creating API Views**
\\ Function-Based API Views \\
>> `from rest_framework.decorators import api_view` --> Just simple and beginner-frendly, Good for small APIs

**Creating Serializers**
Serializer is an object that knows how to convert a model instance, like a product object to Python dictionary
\\ Basic Serializer \\
`from rest_framework import serializers` --> Used when you don't have a model

**Serializing Objects**
Serializing Objects means turning Python objects (usually model instances) into JSON so they can be sent to client.
# Object -> Serializer -> JSON
1. Serialize a single object
# Model Instance
student = Student.objects.get(pk=id) Object
serializer = StudentSerializer(student) Serializer
serializer.data

>>Little Adjustment in the setting.py
# REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False
}