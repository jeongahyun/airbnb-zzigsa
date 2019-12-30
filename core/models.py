from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    """ Time Staped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # make abstractModel
    class Meta:
        abstract = True