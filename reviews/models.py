from django.db import models

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.title
