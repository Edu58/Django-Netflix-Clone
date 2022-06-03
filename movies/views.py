import imp
from urllib import response
from django.shortcuts import redirect, render
from .apis import get_movie, get_trending, get_top_rated, get_genre, get_video, searchMulti
import random
from .forms import CreateUserForm, LoginUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def registerPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('login')
            
    return render(request, 'register.html', {'form': form})


def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = LoginUserForm()
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        user  = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
            
    return render(request, 'login.html', {'form': form})


@login_required(login_url='login')
def profilePage(request):
    return render(request, 'profile.html')


@login_required(login_url='login')
def home(request):
    # banner and trending
    movie = get_trending()
    random_movie = random.randrange(0, 18)
    banner = movie['results'][random_movie]
    trending = movie['results']
    # # top_rated
    # top_rated = get_top_rated()
    #
    # # action movies
    # action = get_genre(28)
    #
    # # comedy movies
    # comedy = get_genre(35)
    #
    # # horror movies
    # crime = get_genre(80)
    #
    # # family movies
    # fantasy = get_genre(14)
    #
    # # documentary movies
    # documentary = get_genre(99)

    return render(request,
                  'index.html',
                  {
                      'banner': banner,
                      'trending': trending,
                      # 'top_rated': top_rated['results'],
                      # 'action': action['items'],
                      # 'comedy': comedy['items'],
                      # 'crime': crime['items'],
                      # 'fantasy': fantasy['items'],
                      # 'documentary': documentary['items'],
                  })


@login_required(login_url='login')
def play(request, movie_id):
    data = get_video(movie_id)
    video_info = data['results'][0]
    youtube_url = f"www.youtube.com/watch?v={video_info['key']}"

    return render(request, 'play.html', {'url': youtube_url})


@login_required(login_url='login')
def search(request):
    
    if request.method == "POST":
        term = request.POST.get('term')
        
        response = searchMulti(term)
    
        results = response['results']
        
        if len(results) > 0 :
            return render(request, 'search.html', {'results': results})

    return render(request, 'search.html')


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')