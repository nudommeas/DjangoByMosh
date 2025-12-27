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
Using Viewset can combine the logic for multiple related views inside a single class. 
The viewset can be imported `from rest_framework.viewsets import ModelViewset`

A viewset that provides default `create()`, `retrieve()`, `update()`,
`partial_update()`, `destroy()` and `list()` actions.
