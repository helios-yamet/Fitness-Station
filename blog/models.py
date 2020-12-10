from django.db import models

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    author = models.TextChoices(null=False, Blank=False)
    content = models.TextField(max_length=500, null=False, blank=False)
    status = models.TextChoices(null=False, Blank=False)

    def __str__(self):
        return self.title
