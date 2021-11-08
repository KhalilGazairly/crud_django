from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.core.mail import send_mail


# Create your views here.


def movie_index(request):
    all_movies = Movie.objects.all()
    print('All Movies : ', all_movies)
    return render(request, 'movie/movie_index.html', context={'movies': all_movies})


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movie/movie_detail.html', context={'movie': movie})


# def movie_create(request):
#     if request.method == 'POST':
#         print(request.POST)
#         movie_name = request.POST.get('name')
#         movie_desc = request.POST.get('desc')
#         movie_likes = request.POST.get('likes')
#         movie_data = {'name': movie_name, 'description': movie_desc, 'likes': movie_likes}
#         print('data =>', movie_data)
#
#         movie_object = Movie.objects.create(name=movie_name, description=movie_desc, likes=movie_likes)
#         print(movie_object)
#
#         return redirect('movie:movie-index')
#
#     return render(request, 'movie/movie_create.html')
#
def movie_create(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print('Yes, is valid')
            form.save()
            return redirect('movie:movie-index')

    return render(request, 'movie/movie_create.html', context={'form': form})


def movie_update(request, pk):
    movie = Movie.objects.get(id=pk)
    form = MovieForm(instance=movie)

    if request.method == 'POST':
        form = MovieForm(data=request.POST, files=request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie:movie-detail', pk=movie.id)

    return render(request, 'movie/movie_update.html', context={'form': form, 'movie': movie})


def movie_delete(request, pk):
    Movie.objects.get(id=pk).delete()
    return redirect('movie:movie-index')
