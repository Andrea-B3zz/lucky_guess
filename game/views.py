import math
from random import random
from django.shortcuts import render

from .models import Guesses, CorrectNumber

# Create your views here.
def mainView(request):
     toDisplay = CorrectNumber.objects.order_by("-id")[:1]
     toDisplay=toDisplay[0]
     test=True

     #if the request is a post, then we're trying to generate a new number, otherwise it's just the homepage
     if request.method == "POST":
          while test:
               numberGenerator = random()
               value = math.floor(1 + (numberGenerator * (toDisplay.maxNumber - 1)))
               allGuesses=Guesses.objects.filter(correctNumber_id=toDisplay.pk)
               
               for x in allGuesses:
                    if x.number==value :
                         test=True
                         break
                    test=False
                    pass
                    
          guess = Guesses()
          guess.number=value
          guess.correctNumber_id=toDisplay.pk
          guess.save()
          return render(
                request,
                "game/mainView.html",
                {'correctNumber': toDisplay,
                 'numberExtracted': guess.number}
            )
     else:
          return render(
                request,
                "game/mainView.html",
                {'correctNumber': toDisplay,
                 'numberExtracted': ""}
            )