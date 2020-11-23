from django.db import models
from datetime import datetime

class User(models.Model):
    uid            = models.CharField(max_length=20)
    email          = models.CharField(max_length=20, unique=True)
    name           = models.CharField(max_length=100)
    given_name     = models.CharField(max_length=100)
    family_name    = models.CharField(max_length=100)
    picture        = models.CharField(max_length=100)
    token          = models.CharField(max_length=30)
    verified_email = models.BooleanField(default=False)
    locale         = models.CharField(max_length=4)
    last_login     = models.DateTimeField(default=datetime.now)
