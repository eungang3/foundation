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

    class Meta:
        db_table = 'movies'

class Actor_movie(models.Model):
    id = models.AutoField(primary_key=True)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        db_table = 'actors_movies'