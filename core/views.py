from django.shortcuts import render

# Create your views here.
def home(request):
    page_title = "Nodelookup | Home"
    context = {
        "page_title":page_title,
    }
    return render(request, 'home.html', context)


def pricing(request):
    page_title = "Nodelookup | Pricing"
    context = {
        "page_title":page_title,
    }
    return render(request, 'pricing.html', context)

def gallery(request):
    page_title = "Nodelookup | Demo Gallery"
    reports = [
        {"channel": "MrBeast", "industry": "Gaming & Entertainment"},
        {"channel": "AliA", "industry": "Gaming"},
        {"channel": "Philip DeFranco", "industry": "News"},
        {"channel": "Gary Vaynerchuk", "industry": "Business"},
    ]
    context = {
        "page_title":page_title,
        "reports":reports
    }
    return render(request, 'gallery.html', context)