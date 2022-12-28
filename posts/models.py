from django.db import models
from django.core.validators import  MinValueValidator
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="")
    day = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)
