from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Guesses, CorrectNumber

# Create your views here.
def mainView(request):
    toDisplay = CorrectNumber.objects.order_by("-id")[:1]
    toDisplay=toDisplay[0]
    return render(
            request,
            "game/mainView.html",
            {'correctNumber': toDisplay}
        )