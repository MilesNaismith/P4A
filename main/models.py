from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(blank=True, upload_to='')
    created_date = models.DateTimeField(
            default=timezone.now)
    

