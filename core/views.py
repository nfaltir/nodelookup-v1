from django.shortcuts import render
from .models import GalleryReport


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
    gallery_reports = GalleryReport.objects.all()
    context = {
        "page_title":page_title,
        "gallery_reports":gallery_reports
    }
    return render(request, 'gallery.html', context)