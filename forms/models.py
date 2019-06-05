from django.db import models
from django.urls import reverse


class TestModel(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    output = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_view', args=[str(self.id)])