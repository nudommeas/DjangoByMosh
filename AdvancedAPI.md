`Views` means HTTP  handling
A view is the place where HTTP request( GET , POST , PUT , PATCH , DELETE ) are received and handled.

\\ ------------------------------------ ------------------------------------ \\ 

**Class-based View**
--> Using `APIVIEW`
--> the incoming request is automatically sent to one of these methods, depending on its method.
--> APIView handler method such as .get() , .post() , .put() , .patch() , .delete()
--> .as_view() set in Url.py

\\ ------------------------------------ ------------------------------------ \\ 

**Mixins**
The mix classes can be imported `from rest_framework.mixins`

The Mixin classes provide the actions that are used to provide the basic view behavior. Note that the mixin classes provide action methods rather than defining the handler methods, such as .get() and .post() directly.

A Mixin is just a class that adds methods to your view.
# For Example: When the  `ListModelMixin`class is being called. This automatically adds a `.list()` method to the view.

# The Primary mixins include:
--> `ListModelMixin`: Provide an `.list()` method that handles listing a queryset of objects.
--> `CreateModelMixin`: Provide a `.create()` method that handles creating a new object.
--> `RetrieveModelMixin`: Provide a `.retrieve()` method that handles retrieving a single object
--> `UpdateModelMixin`: Provide an `.update()` method that handles updating an existing object.
--> `DetroyModelMixin`: Provide a `.destroy()` method that handles deleting an object

\\ ------------------------------------ ------------------------------------ \\ 

**Generic API Views**
They combine the functionality of `APIview` with specific mixins to provide ready-to-use views for common databse interaction. This significantly reduces the amount of code needed compared to writing each method (e.g, `get`,`post`,`put`,`delete`) manually.

\\ Core Generic View Classes \\
# queryset
# serializer_class
`GenericAPIView`: This is the base class for all generic views. It provides core functionality such as `get_object`,`get_queryset`, `get_serializer_class`, and pagination. It doesn't provide any HTTP method handlers such as .get() or .post() directly. 
# Means: GenericAPIView doesn't provide  the HTTP method to the view
# because Mixins handle of those things. It provides:
--> `ListModelMixin`: Used for read-only endpoints to represent a ccollection of model instances.
--> `CreateModelMixin` Used for create-only endpoints
--> `RetrieveModelMixin` Used for read-only endpoints to represent a single model instance.
--> `UpdateModelMixin` Used for update-only endpoints for a single model instance.
--> `DetroyModelMixin` Used for delete-only endpoints for a single model instance.
-------------------------------------------------------------------------------------------------------
--> `ListCreateAPIView`: Combines `ListAPIView` and `CreateAPIView` for read-write endpoints representing a collection of model instances.
--> `RetrieveUpdateAPIView`: Combines RetrieveAPIView and DestroyAPIView for read-delete endpoints representing a single model instance.
--> `RetrieveUpdateDestroyAPIView`: Provides complete read-write-delete operations for a single model instance.

# For Example: `ListCreateAPIView` automatically handles the `GET` request to list objects and the `POST` request to create objects, using `queryset` to fetch data and `serializer_class` to serialize/deserialize it.

\\ ------------------------------------ ------------------------------------ \\ 

**ViewSets**

# Using Viewset can combine the logic for multiple related views such as `list` , `retrieve` , `create` , `update` , `destroy` inside a single class. 

The viewset can be imported `from rest_framework.viewsets import ModelViewset`

# `GenericViewset`: Extends `ViewSet` and integrates with DRF's `GenericAPIView` base class, providing `get_object`, `get_queryset`, `get_serializer`, and other methods but without specific action implementations. This is useful when you want to define custom actions or have full control over the actions.

# `ModelViewSet` Extends `GenericViewSet` and includes implementations for `list`, `retrieve`, `create`, `update`, `destroy`actions, based on a model. This is the most commonly used `ViewSet` for typical CRUD operations on a single model.

For Example of `ModelViewSet`:

class BookViewSet(ModelViewSet): 
# This means: The class BookViewSet inherit from ModelViewSet. When this single class registered with a router, automatically handles:
`GET /books/`: List all books(`list` action)
`POST /books/` Create a new book (`create` action)
`GET /books/{id}`: Retrieve a single book (`retrieve` action)
`PUT /books/{id}`: Update a book (`update` action)
`PATCH /books/{id}`: Partially update a book (`partial_update` action)
`DELETE /books/{id}`: Delete a book (`destroy` action)

\\ ------------------------------------ ------------------------------------ \\ 

**Understanding Filter() method**

# Mostly used for filter across relationship using the `double underscore (__)` syntax
# This works for `ForeignKey`, `ManyToManyField`, and `OneToOneField` relationships. 

\\ How to filter Across Relationship? \\
# To span a relationship, you use the `field name` of the related `model`(e,g. `Blog model`), followed by a double underscore, and then the `field name` on the related model you want to filter on (e,g. `Entry model`).

from django.db import models

# class Blog(models.Model):
    name = models.CharField(max_length=100)

# class Entry(models.Model):
    headline = models.CharField(max_length=255)
    pub_date = models.DateField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

Filter Example: 
# Filter `Entry` objects based on the `name` of the related `Blog`

# `Entry`.objects.`filter`(blog__name='Beatles Blog')--> This retrieves all Entry objects associated with a Blog named 'Beatles Blog'.
# The lowercase name of the related model (blog) is used for the reverse relationship lookup.

# Filter `Blog` objects based on the headline of a related `Entry`

# if `Product`.objects.`filter`(collection__id=kwargs['pk']).count() > 0:
    return Response({'errors': 'Collection cannot be delete with associated product_count'})

\\ ------------------------------------ ------------------------------------ \\ 

**Understanding DRF Routers**

`DefaultRouter`: It automatically generates URL patterns for standard CRUD operations and also includes an API root view that lists all registered resources, along with an optional format suffix pattern. This makes it suitable for most API projects. This route also inspects a ViewSet and determine the necessary URL patterns based on the method defined.
# (e,g. `list`, `retrieve`, `create`, `update`, `destroy`)

# API Root View:  
This is the output of Api root view
{
    "products": "http://127.0.0.1:8000/store/products/",
    "collections": "http://127.0.0.1:8000/store/collections/"
}

\\ ------------------------------------ ------------------------------------ \\ 

**Nested Routers**
# INSTALLATION: pip install drf-nested-routers

1. Defining Routers

# To create a nested route, you first define a standard DRF router and then wrap it in a `NestedDefaultRouter`. 
`router = routers.DefaultRouter()`

# Initial Router: You register the parent resource (e.g, `products`) with a standard `DefaultRouter`.
`router.register(r'products', views.ProductViewset)`

# Nested Router: You then initialise a `NestedDefaultRouter`, passing in the `parent router` and the `parent prefix`. The `lookup` argument defines the prefix for the keyword argument used in the URL (e.g,`lookup='product'` result in `product_pk`)
`product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')`

# Registration: Finally, you register the child resource (e.g, `reviews`) to this new nested router.
`product_router.register('reviews', views.ReviewViewSet, basename='product-review')`
The resulting URLs will look like `products/{product_pk}/reviews` and `products/{product_pk}/reviews/{pk}`

\\ ------------------------------------ ------------------------------------ \\ 

**get_queryset**
1️⃣ What is get_queryset?
# It is a method in Django/DRF views and Viewsets that defines which objects are returned for a request. 
# It decides WHAT data this API endpoint is allowed to return.
2️⃣ Why does get_queryset() exist?
# becuase different requests may need different data.
Note: You can not do this with a static `queryset = Product.objects.all()`
3️⃣ Mostly, using for `query parameters`
4️⃣ Filtering by URL parameters(kwargs), Mostly used in `Nested Routes`,` /collections/3/products/ `
# Summary 
- get_queryset() dynamically controls which database objects an API endpoint returns, based on request data, user, or URL parameters.

# get_serializer_context() - we use a context object to provide additional data to a serializer.

\\ ------------------------------------ ------------------------------------ \\ 

**Filter against query parameters**

# What is Filter against query parameters mean?
✅ It means:
# Using Values from the URL query string to filter database results
Example URL:
`GET /products/?collection_id=3&min_price=100` Collection and min_price are query parameters

# Why do we use filtering with query parameters?
✅ APIs must be flexible:
    Clients (frontend) choose what data they want

# How to access query parameters in DRF?
Using `request.query_params`

# Why use .get() instead of []?
✔ Safe if param doesn’t exist
❌ request.query_params['collection'] → error if missing

# When should we use it?
Use filtering against query params when:
- List endpoints
- Search
- Filtering by category
- Filtering price/data/status

\\ ------------------------------------ ------------------------------------ \\ 

**Generic Filter**

Using Django Filter Library - pip install django-filter

INSTALLED_APPS = [
    ...
    'django_filters',
]
`from django_filters.rest_framework import DjangoFilterBackend`

# A FilterSet specifies which fields of a model can be filtered and how they should be filtered.
Creating a file `filter.py` to define `Filterset` within your app.
`from django_filters.rest_framework import Filterset`

# Common Lookup fields to Use
--Containment and String Matching:
- __contains :  Checks if the field value contains the specified value, case-sensitive.
- __icontains : Case-insensitive version of `contains`. This is commonly used for search functionality.
- __startswith : Checks for a case-sensitive start of the string.
- __istartswith : Case-insensitive version of `startswith`.
- __endswith :  Checks for a case-sensitive end of the string.
- __iendswith : Case-insensitive version of `endswith`.
--Comparisons:
- gt : Greater than
- gte : Greater than or equal to
- lt : Less than
- lte : Less than or equal to
- range : Checks if the field value is between two values.
--Date and Time Lookups
- Year , Month , Day : Extracts the year, month, or day part from a date or datetime field for comparison.

\\ ------------------------------------ ------------------------------------ \\ 

**Searching**
`from rest_framework.filters import SearchFilter`

# Include `SearchFilter` inside the `filter_backends = []`
# search_fields = ['title', 'description']

\\ ------------------------------------ ------------------------------------ \\ 

**Sorting data**
`from rest_framework.filters import SearchFilter, OrderingFilter`
ordering_fields = ['unit_price]
- ascending
- descending

**GUID/UUID**

# What is a GUID/UUID?    
A UUID is a globally unique identifier
# Why use GUID?
✅ Benefits
Harder to guess (better security)
Safe for public APIs
No ID collision across systems
Great for distributed systems
Professional / industry standard