from django.shortcuts import render
from .apis import get_movie


# Create your views here.
def home(request):
    movie = get_movie()
    print(movie)
    return render(request, 'index.html')
