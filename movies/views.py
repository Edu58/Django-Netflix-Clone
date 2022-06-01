from django.shortcuts import render
from .apis import get_movie, get_trending, get_top_rated, get_genre
import random


# Create your views here.
def home(request):
    # banner and trending
    movie = get_trending()
    random_movie = random.randrange(0, 11)
    banner = movie['results'][random_movie]
    trending = movie['results']

    # top_rated
    top_rated = get_top_rated()

    # action movies
    action = get_genre(28)

    # comedy movies
    comedy = get_genre(35)

    # horror movies
    crime = get_genre(80)

    # family movies
    fantasy = get_genre(14)

    # documentary movies
    documentary = get_genre(99)

    return render(request,
                  'index.html',
                  {
                      'banner': banner,
                      'trending': trending,
                      'top_rated': top_rated['results'],
                      'action': action['items'],
                      'comedy': comedy['items'],
                      'crime': crime['items'],
                      'fantasy': fantasy['items'],
                      'documentary': documentary['items'],
                  })
