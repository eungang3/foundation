from django.db import models

# Create your models here.
class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    

    class Meta:
        db_table = 'actors'