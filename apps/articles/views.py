
from django.shortcuts import render, redirect
from .models import Genre,Game,Review
from apps.articles.forms import ReviewForm


def home(request):
    games = Game.objects.all()
    return render(request, 'home.html',{'games':games})

def shop(request):
    return render(request, 'shop.html')

def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'product-details.html')


def review_list(request):
    games = Game.objects.all()
    return render(request, 'home.html', {'games': games})
    

def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'create_review.html',{'form': form})
    else:
        form = ReviewForm()
        return render(request,'create_category.html',{'form':form})
