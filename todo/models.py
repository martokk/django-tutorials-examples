from django.db import models


class Tasks(models.Model):
    task = models.TextField(max_length=200)

