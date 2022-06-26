from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title