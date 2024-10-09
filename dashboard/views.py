from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from user_request.models import UserRequest
from django.contrib.auth.models import User

@login_required
def dashboard(request):
    page_title = "Dashboard"
    user_requests = UserRequest.objects.filter(user=request.user) 

    context = {
        "page_title":page_title,
        "user_requests":user_requests,
    }
    return render(request, "dashboard.html", context)


def user_request_detail(request, id):
    page_title = "Request Details"
    request_detail = get_object_or_404(UserRequest, id=id)
    context = {
        "page_title":page_title,
        "request_detail":request_detail,
    }
    return render(request, 'request_details.html', context)