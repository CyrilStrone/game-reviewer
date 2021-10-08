from django import template
from games.models import Category, Game, Genre


register = template.Library()


@register.simple_tag()
def get_genries():
    """Вывод всех жанров"""
    return Genre.objects.all()


@register.inclusion_tag('games/tags/last_game.html')
def get_last_games(count=2):
    games = Game.objects.order_by("-id")[:count]
    return {"last_games": games}