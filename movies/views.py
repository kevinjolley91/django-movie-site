from django.http import HttpResponse
from django.template import loader

from .models import Movie


def index(request):
    latest_movie_list = Movie.objects.all()
    template = loader.get_template("movies/index.html")
    context = {
        "latest_movie_list": latest_movie_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, movie_id):
    return HttpResponse("You're looking at movie %s." % movie_id)
