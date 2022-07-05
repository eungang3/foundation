from django.db import models

# Create your models here.
class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'actors'

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()
    actor = models.ManyToManyField(Actor)

    class Meta:
        db_table = 'movies'
