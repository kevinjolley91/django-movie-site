from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.title
