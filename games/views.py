from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q, Avg
from django.http import JsonResponse

from .models import Game, Genre, Category, Developer
from .forms import ReviewForm, RatingForm, Rating
# Create your views here.

class GenreYear:
    """Жанры и года выхода фильмов"""
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Game.objects.filter(draft=False).order_by('year').values("year").distinct()
		

class GamesView(GenreYear, ListView):
	"""Список игр"""
	model = Game
	queryset = Game.objects.filter(draft=False)
	template_name = "game/games.html"

	paginate_by = 15




class GameDetailView(GenreYear, DetailView):
    """Полное описание игры"""
    model = Game
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        return context

class GenreView(GenreYear, DetailView):
    model = Genre
    template_name = "games/genre.html"
    slug_field = "url"


class AddReview(View):
	"""Отзывы"""
	def post(self, request, pk):
		form = ReviewForm(request.POST)
		game = Game.objects.get(id=pk)
		if form.is_valid():
			form = form.save(commit=False)
			if request.POST.get("parent", None):
				form.parent_id = int(request.POST.get("parent"))
			form.game_id = pk
			form.save() 

		return redirect(game.get_absolute_url())

class DeveloperView(GenreYear, DetailView):
	"""Полное описание разработчика или публ"""
	model = Developer
	template_name = 'games/developer.html'
	slug_field = "name"

class FilterGamesView(GenreYear, ListView):
    """Фильтр игр"""
    paginate_by = 6

    def get_queryset(self):
        queryset = Game.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genre__in=self.request.GET.getlist("genre"))
        ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        return context

class AddStarRating(View):
    """Добавление рейтинга фильму"""
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                game_id=int(request.POST.get("game")),
                user=request.POST.get("username"),
                defaults={'star_id': int(request.POST.get("star"))},

            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)



        

class Search(ListView):
    """Поиск фильмов"""
    paginate_by = 4

    def get_queryset(self):
        return Game.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context