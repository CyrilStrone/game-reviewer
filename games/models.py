from django.db import models
from datetime import date
from django.urls import reverse

class Category(models.Model):
    """Возрастной рейтинг"""
    name = models.CharField("Возрастной рейтинг", max_length=150)
    age = models.CharField('Разрешенный возраст', max_length=20)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Genre(models.Model):
    """Жанр"""
    name = models.CharField("Жанр", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
	

    def get_absolute_url(self):
        return reverse('genre_detail', kwargs={"slug": self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
		

class Developer(models.Model):
    """Разработчик и издатель"""
    name = models.CharField('Имя', max_length=100)
    date = models.DateField('Дата основания', default=date.today)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to="developers/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('developer_detail', kwargs={"slug": self.name})


    class Meta:
        verbose_name = "Разработчик и издатель"
        verbose_name_plural = "Разработчики и издатели"

class Game(models.Model):
    """Игры"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="posters/")
    date = models.DateField("Дата выхода", default=date.today)
    year = models.PositiveSmallIntegerField("Год выхода", default=2021)
    developer = models.ManyToManyField(Developer,verbose_name='разработчик', related_name="game_developer")
    publisher = models.ManyToManyField(Developer,verbose_name='издатель', related_name="game_publisher")
    category = models.ManyToManyField(Category, verbose_name="категории")
    genre = models.ManyToManyField(Genre, verbose_name="жанр")
    url = models.SlugField(max_length=130, unique=True)
    trailer = models.CharField("Трейлер", max_length=200, blank=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("game_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)


    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"



class GameShots(models.Model):
    """Кадры из игры"""
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to="game_shots/") 
    game = models.ForeignKey(Game, verbose_name="Игры", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из игры"
        verbose_name_plural = "Кадры из игр"     

class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.PositiveSmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""

    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE,verbose_name="звезда")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="игра")
    user = models.CharField("Имя пользователя", max_length=150)

    def __str__(self):
        return f"{self.star} - {self.game}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    game = models.ForeignKey(Game, verbose_name="игра", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.game}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
