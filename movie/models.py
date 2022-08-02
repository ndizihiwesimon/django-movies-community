from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255, blank=False)
    body = models.TextField(blank=False)
    poster = models.ImageField(upload_to="Posters/")
    genre = models.CharField(max_length=100, blank=False)
    actors = models.CharField(max_length=100, blank=False)
    trailer = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movies")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title