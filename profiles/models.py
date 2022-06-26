from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
# Create your models here.
class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    img = models.ImageField(default="default.jpg",upload_to="profile_pics")
    def __str__(self):
        return self.user.username
     
    