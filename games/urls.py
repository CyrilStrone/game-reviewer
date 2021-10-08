from django.urls import path
from . import views

urlpatterns = [
	path("", views.GamesView.as_view(), name="main_page"),
	path("filter/", views.FilterGamesView.as_view(), name='filter'),
	path("search/", views.Search.as_view(), name='search'),
	path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),

	path("genre/<slug:slug>/", views.GenreView.as_view(), name="genre_view"),
	path("<slug:slug>/", views.GameDetailView.as_view(), name="game_detail"),



	path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
	path("developer/<str:slug>/", views.DeveloperView.as_view(), name="developer_detail"),

]