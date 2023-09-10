from django.db import models

# Create your models here.
class CaughtPokemon(models.Model):
    name=models.CharField(max_length=100)
    level=models.IntegerField(default=0)
    height=models.DecimalField(max_digits=5 , decimal_places=3,null=True,blank=True)

    def __str__(self):
        return self.name