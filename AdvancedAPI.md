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