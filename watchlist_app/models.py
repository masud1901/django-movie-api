from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.TextField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self) -> str:
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.TextField(max_length=200)
    platform = models.ForeignKey(
        StreamPlatform, on_delete=models.CASCADE, related_name="watchlist"
    )
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    rating = models.PositiveBigIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    watchlist = models.ForeignKey(
        WatchList, on_delete=models.CASCADE, related_name="reviews"
    )
    description = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{str(self.rating)} - {self.watchlist.title}"
