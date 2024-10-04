from django.shortcuts import render

# Create your views here.
def dashboard(request):
    page_title = "Dashboard"

    context = {
        "page_title":page_title
    }
    return render(request, "dashboard.html", context)