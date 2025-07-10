from django.db import models

class PlaceCategory(models.Model):
    name = models.CharField(
        max_length=100,
    )
    short_description = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"



class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to='places/',
        blank=True,
        null=True
    )
    created_add = models.DateField(
        auto_now_add=True
    )
    updated_add = models.DateTimeField(
        auto_now=True
    )
    views_count = models.PositiveIntegerField(
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "sight"
        verbose_name_plural = "attractions"

