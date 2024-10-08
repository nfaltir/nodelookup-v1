from django.shortcuts import render
from user_request.models import UserRequest
from django.contrib.auth.models import User

# Create your views here.
def dashboard(request):
    page_title = "Dashboard"
    user_requests = UserRequest.objects.filter(user=request.user) 

    context = {
        "page_title":page_title,
        "user_requests":user_requests,
    }
    return render(request, "dashboard.html", context)