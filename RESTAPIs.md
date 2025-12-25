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

# `Serializers: Transforming Django Models to JSON`

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

**Creating Custom Serializer Fields**
Custom serilizer fields let you control exactly how a value is calculated, displayed, or validated in the JSON output
`SerializerMethodField()` used for read-only computed fields

**Serializing Relationship**
1. Primary Key Related Field(`PrimaryKeyRelatedField`)
Arguments:
`queryset` - The queryset used for model instance lookups when validating the field input
2. String Related Field(`StringRelatedField`)
3. Nested Serializers --> This creates a nested JSON structure
# class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
# class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    collection = CollectionSerializer()
# Output:
    {
        "id": 648,
        "title": "7up Diet, 355 Ml",
        "unit_price": 79.07,
        "price_with_tax": 86.977,
        "collection": {
            "id": 5,
            "title": "Stationary"
        }
    },
4. Hyperlinked Related Field(`HyperlinkedRelatedField`)
Arguments:
`view_name` - The views naem that should be used as the target of the relationship. Set it in the Urls.py 
`queryset` - The queryset used for model instance lookups when validating the field input
`lookup_field` - Default is `pk`.

**Model Serializers**
Model serializers are a shotcut for creating serializers that work directly with Django models.
`Model` = database structure
`ModelSerializer` = automatic serializer for that model. Means: A ModelSerializer automatically converts a Djang model instance into JSON.
<class Meta:
    model
    fields
def validate()
def create()
>

**Deserializing Objects**
Deserializing objects meanns converting incoming JSON Data into Python objects (usaully Model Instances).
# JSON -> Serializer -> Python Object/Model
---------------
# For Example:
-->The Client wants to create a new product
--> To do this, it should send a POST request to the products endpoint <POST /products >
--> and In the body of the request should include a product object
{ \\ Here's the request body \\
    "title": "Hello", 
    "price": 10       
}
--> So on the server, we have to read the data in the body of the request and deserialize it so we get a product object and store it in the Database

# serialize = ProductSerializer(data=request.data) 
What DRF does:
1. Takes JSON from the client requests --> request.data
2. Converts the client data into Python data
3. Validates it
4. Creates or updates a model object

# Data validation
Summary: Data Validation ensures only correct and safe data is saved to the database.

\\ reqest.data -> deserializer -> is_valid() -> validated_data -> save() \\

# if serializer.is_valid(): # Validate the incoming data
#     serializer.validated_data # .validated_data holds the cleaned, valid incoming after the .is_valid() is TRUE
      it holds as a dictionary

\\ First Approach \\
# if errors 
# from rest_framework import Product
# Return Response(serializer.error, status=status.Http)

\\ Second Approach \\
# serializer = ProductSerializer(data=request.data)
# serializer.is_valid(raise_exception=True)
# serializer.validated_data
# return Response('OK')

**Updating an Existing Object**
\\ PUT method \\
When updating, you pass the existing model instances as the first argument to the serializer and the new data as the `data` keyword argument.
# product = get_object_or_404(Product, pk=id) # getting the existing users data in the datase
# serializer = ProductSerializer(product, data=request.data) # data=request.data: new data submiited by the client or user

**Deleting Objects**