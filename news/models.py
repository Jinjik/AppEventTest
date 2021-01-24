from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField()

    def __str__(self):
        return self.title
