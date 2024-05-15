from django.db import models

# Create your models here.
class CorrectNumber(models.Model):
    number = models.IntegerField()
    maxNumber = models.IntegerField()
    guessed = models.BooleanField(default=False)
    numberOfGuesses = models.IntegerField(default=0)

class Guesses(models.Model):
    correctNumber = models.ForeignKey(CorrectNumber, on_delete=models.CASCADE)
    number = models.IntegerField(unique=True)
