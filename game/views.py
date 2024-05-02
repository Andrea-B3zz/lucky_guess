import math
from random import random
from django.shortcuts import render

from .models import Guesses, CorrectNumber

# Create your views here.
def newNumber(request):
     correct = CorrectNumber.objects.order_by("-id")[:1]
     correct=correct[0]
     test=True

     allGuesses=Guesses.objects.filter(correctNumber_id=correct.pk)
     while test:
          test=False
          numberGenerator = random()
          value = math.floor(1 + (numberGenerator * (correct.maxNumber - 1)))
          for x in allGuesses:
               if x.number==value :
                    test=True
                    break
                    
     guess = Guesses()
     guess.number=value
     guess.correctNumber_id=correct.pk
     guess.save()
     if guess.number==correct.number:
         return render(
          request,
          "game/winningPage.html",
          {'correctNumber': correct,
          'numberExtracted': guess.number}
          )
     else:
          return render(
               request,
               "game/gamePage.html",
               {'correctNumber': correct,
               'numberExtracted': guess.number}
          )

def newGame(request):
     allGuesses=Guesses.objects.all()
     allGuesses.delete()
     correctNumber = CorrectNumber()
     correctNumber.maxNumber=100
     numberGenerator = random()
     value = math.floor(1 + (numberGenerator * correctNumber.maxNumber))
     correctNumber.number=value
     correctNumber.save()
     print("Ciao")

     return render(
          request,
          "game/gamePage.html",
          {'correctNumber': correctNumber}
     )

def start(request):
     correct = CorrectNumber.objects.order_by("-id")[:1]
     correct=correct[0]
     return render(
          request,
          "game/gamePage.html",
          {'correctNumber': correct}
     )