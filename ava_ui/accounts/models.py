from django.db import models


class UserToken(models.Model):
    token = models.CharField(max_length=300)
    owner = models.CharField(max_length=300)

    def __str__(self):
        return self.owner
