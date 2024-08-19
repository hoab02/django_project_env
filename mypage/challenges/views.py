from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenge = {
    "january": "January Now!",
    "february": "February Now!",
    "march": "March Now!",
    "april": "April Now!",
    "may": "May Now!",
    "june": "June Now!",
    "july": "July Now!",
    "august": "August Now!",
    "september": "September Now!",
    "october": "October Now!",
    "november": "November Now!",
    "december": "December Now!"
}

def index(request):
    list_items = ""
    months = list(monthly_challenge.keys())
    
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("monthly_", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"   
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    
    return render(request, "challenges/index.html", {
        "months": months
    })

# Create your views here.
def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge.keys())
    
    if month > len(months):
       return HttpResponseNotFound("Invalid month!") 
   
    redirect_month = months[month-1]
    
    redirect_path = reverse("monthly_", args=[redirect_month])
    
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request, month):
    try:   
        text_ = monthly_challenge[month]
        # data_response = f"<h1>{text}</h1>"
        # data_response = render_to_string("challenges/challenge.html")
        return render(request, "challenges/challenge.html", {
            "text": text_,
            "month_challenge": month
        })
        # return HttpResponse(data_response)
    except:
        return HttpResponseNotFound("<h1>Error!</h1>")
        