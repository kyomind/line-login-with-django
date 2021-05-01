from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    photo_url = models.CharField(max_length=256)
    stats_info = models.CharField(max_length=128)

    def __str__(self):
        return self.name