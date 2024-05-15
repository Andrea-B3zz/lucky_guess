import math
from random import random
from django.shortcuts import render
from .models import Guesses, CorrectNumber

def newNumber(request):
     correct = CorrectNumber.objects.order_by("-id")[:1]
     correct=correct[0]

     if correct.guessed==True:
          return render(
          request,
          "game/startPage.html"
     )

     correct.numberOfGuesses+=1
     correct.save()

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
         correct.guessed=True
         correct.save()
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
     correct = CorrectNumber.objects.order_by("-id")[:1]
     correct=correct[0]
     if(correct.numberOfGuesses==0):
          return render(
          request,
          "game/gamePage.html",
          {'correctNumber': correct}
     )
     allGuesses=Guesses.objects.all()
     allGuesses.delete()
     correctNumber = CorrectNumber()
     correctNumber.maxNumber=100
     numberGenerator = random()
     value = math.floor(1 + (numberGenerator * correctNumber.maxNumber))
     correctNumber.number=value
     correctNumber.save()

     return render(
          request,
          "game/gamePage.html",
          {'correctNumber': correctNumber}
     )

def start(request):
     correct = CorrectNumber.objects.order_by("-id")[:1]
     if len(correct)!=0:
          correct=correct[0]
          if(correct.guessed==False):
               return render(
                    request,
                    "game/gamePage.html",
                    {'correctNumber': correct}
               )
     return render(
          request,
          "game/startPage.html"
     )