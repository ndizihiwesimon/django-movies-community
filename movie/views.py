from operator import attrgetter
from django.db.models import Q
from django.shortcuts import render, redirect
from movie.models import Comment, Movie

# Create your views here.

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


def movie_detail(request, bid):
    context = Movie.objects.get(id=bid)
    Ge = context.Genre
    context2 = Movie.objects.filter(Genre=Ge).exclude(id=bid)
    context3 = Movie.objects.order_by('Genre').distinct('Genre')
    context4 = Comment.objects.filter(Movie=bid)
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
