from operator import attrgetter
from django.db.models import Q
from django.shortcuts import render, redirect
from movie.forms import MovieForm
from movie.models import Comment, Movie
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def movie_create(request):
    form = MovieForm()
    context = {
        "form": form,
    }
    if request.method == 'POST':
        movie_form = MovieForm(request.POST, request.FILES)
        if movie_form.is_valid():
            movie_post = movie_form.save(commit=False)
            movie_post.author = request.user
            movie_post.save()

            print()
            print()
            print("Saved successfully")
            print()
            return redirect('movie-list')
        else:
            context = {
                "form": movie_form,
                "errors": movie_form.errors,
            }
            print()
            print()
            print("Error cannot submit form")
            print()
            return render(request, 'movies/movie-create.html', context)
    return render(request, 'movies/movie-create.html', context)


def movie_list(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    movies = sorted(movie_search(query), key=attrgetter(
        'created_at'), reverse=True)
    context['movies'] = movies
    return render(request, "movies/movie-list.html", context)


def movie_detail(request, pk):
    context = Movie.objects.get(id=pk)
    Ge = context.genre
    context2 = Movie.objects.filter(genre=Ge).exclude(id=pk)
    context3 = Movie.objects.order_by('genre').distinct('genre')
    context4 = Comment.objects.filter(movie=pk)
    both = {'related': context2, 'details': context,
            'cats': context3, 'comments': context4}

    if request.method == 'POST':
        if request.POST.get('names') and request.POST.get('comment'):
            saveComment = Comment()
            saveComment.user = request.user
            saveComment.body = request.POST['comment']
            saveComment.movie = context
            saveComment.save()
            print('Comment sent successfully!')
        else:
            print('Something went wrong')
            return redirect('movie-detail')
    return render(request, "movies/movie-details.html", both)


def movie_search(query=None):
    queryset = []
    queries = query.split(", ")
    for q in queries:
        posts = Movie.objects.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q) |
            Q(genre__icontains=q)
        ).distinct()

        for post in posts:
            queryset.append(post)

    return list(set(queryset))

