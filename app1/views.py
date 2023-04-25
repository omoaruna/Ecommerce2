from django.shortcuts import render
from .models import Category

def home_page(request):
    all_categories = Category.objects.all()

    context = {
       "all_categories" : all_categories
    }
    return render(request, "app1/index2.html", context)

# Create your views here.
