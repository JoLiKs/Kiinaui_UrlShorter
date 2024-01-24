from django.db import models

class UrlModel(models.Model):

    user_url = models.TextField()
    short_url = models.TextField()