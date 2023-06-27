from django.shortcuts import render
from django.http import Http404, HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse



monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}
# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {"title":"Homp Page", "months":months})


def monthly_challenge_numbers(request, month):
    month_list = list(monthly_challenges.keys())
    if month > len(month_list):
        return HttpResponseBadRequest("Month Not Valid")
    redirect_month = month_list[month-1]
    rev = reverse("monthly_challenge", args=[redirect_month])
    return HttpResponseRedirect(rev)
    

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenges.html", {"text": challenge_text, "title":month})
    except:
        raise Http404
    
    
