from django.db import models
from admin_app.choices import CategoryChoices, RoomsChoices


class Movies(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    director = models.CharField(max_length=100, blank=False, null=False)
    casting = models.CharField(max_length=100, blank=False, null=False)
    duration = models.CharField(max_length=100, blank=False, null=False)
    category = models.CharField(choices=CategoryChoices.choices, max_length=50, blank=False, null=False)
    rating = models.IntegerField(blank=False, null=False)


class Rooms(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(choices=RoomsChoices.choices, max_length=100, blank=False, null=False)
    seats = models.IntegerField(blank=False, null=False)
    three_d = models.BooleanField(blank=False, null=False)


class Teather(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    location = models.CharField(max_length=100, blank=False, null=False)
    titles = models.ForeignKey("Movies", on_delete=models.CASCADE)
    rooms = models.ForeignKey("Rooms", on_delete=models.CASCADE)
