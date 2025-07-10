from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    slug = models.CharField(max_length=100 , unique=True)
    icon = models.ImageField(upload_to='genres/',blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Game(models.Model):
    title = models.CharField(max_length=200)  # Название игры
    slug = models.SlugField(max_length=200, unique=True)  # URL (например, "the-witcher-3")
    description = models.TextField()  # Полное описание
    release_date = models.DateField()  # Дата выхода
    age_rating = models.CharField(max_length=10,)  # Возрастной рейтинг ("E", "T", "M")
    developer = models.CharField(max_length=100)  # Разработчик
    publisher = models.CharField(max_length=100)  # Издатель
    cover_image = models.ImageField(upload_to='games/covers/')  # Обложка игры
    trailer_url = models.URLField(blank=True)  # Ссылка на трейлер (YouTube)

    # Связи с другими моделями:
    genres = models.ManyToManyField(Genre)  # Одна игра → несколько жанров


class Review(models.Model):
    email = models.EmailField()
    fio = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.PositiveIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'




