from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    cover_image = models.ImageField(upload_to='games/covers/')  # Обложка игры
    trailer_url = models.URLField(blank=True)  # Ссылка на трейлер (YouTube)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Review(models.Model):
    email = models.EmailField()
    user_name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.PositiveIntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(5)]
)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'




