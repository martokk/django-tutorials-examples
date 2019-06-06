from django.db import models


class FormSetModel(models.Model):
    keyword = models.CharField(max_length=50)
    condition = models.CharField(max_length=10, choices=(
        ('in', 'in'),
        ('not_in', 'not in'),
    ))
    source = models.CharField(max_length=10, choices=(
        ('feed', 'Feed'),
        ('title', 'Title'),
        ('body', 'Body'),
        ('link', 'Link'),
        ('tag', 'Tags'),
    ))
    action = models.CharField(max_length=10, choices=(
        ('hide', 'Hide Article'),
        ('show', 'Show Article'),
    ))

    # def __str__(self):
    #     return f"IF [{self.keyword}] [{self.condition}] [{self.source}]; THEN [{self.action}]"
