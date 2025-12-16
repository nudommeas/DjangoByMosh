from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    # What tag applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #Type (product, video , article) --> using the type, we can find the table
    #ID using the ID, we can find the record
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class LikeItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')