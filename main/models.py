from django.db import models


# Create your models here.

class Settings(models.Model):
    use_example_link = models.BooleanField(default=False)
    example_link = models.CharField(max_length=255, blank=True, null=True)
