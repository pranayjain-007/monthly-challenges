from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "To Do 1",
    "february": "To Do 2",
    "march": "To Do 3",
    "april": "To Do 4",
    "may": "To Do 5",
    "june": "To Do 6",
    "july": "To Do 7",
    "august": "To Do 8",
    "september": "To Do 9",
    "october": "To Do 10",
    "november": "To Do 11",
    "december": "To Do 12"
}


def index(request):
    try:
        months = list(monthly_challenges.keys())
        return render(request, "challenges/index.html", {
            "months": months
        })
    except:
        raise Http404()


def challenges_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        monthly_challenge = months[month - 1]
        redirect_path = reverse("month-challenge", args=[monthly_challenge])
        return HttpResponseRedirect(redirect_path)
    except:
        raise Http404()


def challenges_by_name(request, month):
    try:
        months = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "challenge" : months
        })
    except:
        raise Http404()
