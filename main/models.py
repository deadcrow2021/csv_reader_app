from django.db import models


class Deals(models.Model):
    customer = models.CharField(max_length=300, blank=True, null=True)
    item = models.CharField(max_length=300, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()
 