from django.db import models
from django.contrib.auth.models import User

class Anime(models.Model):
    anime_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    title_english = models.CharField(max_length=255, null=True, blank=True)
    title_japanese = models.CharField(max_length=255, null=True, blank=True)
    title_synonyms = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    source = models.CharField(max_length=50, null=True, blank=True)
    episodes = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    airing = models.BooleanField(default=False)
    aired_string = models.CharField(max_length=255, null=True, blank=True)
    aired = models.JSONField(null=True, blank=True)  # You can use JSONField to store dates
    duration = models.CharField(max_length=50, null=True, blank=True)
    rating = models.CharField(max_length=50, null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    scored_by = models.IntegerField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    popularity = models.IntegerField(null=True, blank=True)
    members = models.IntegerField(null=True, blank=True)
    favorites = models.IntegerField(null=True, blank=True)
    background = models.TextField(null=True, blank=True)
    premiered = models.CharField(max_length=50, null=True, blank=True)
    broadcast = models.CharField(max_length=50, null=True, blank=True)
    related = models.JSONField(null=True, blank=True)  # Storing the related anime as JSON
    producer = models.CharField(max_length=255, null=True, blank=True)
    licensor = models.CharField(max_length=255, null=True, blank=True)
    studio = models.CharField(max_length=255, null=True, blank=True)
    genre = models.CharField(max_length=255, null=True, blank=True)
    opening_theme = models.TextField(null=True, blank=True)
    ending_theme = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


# class AnimeCharacter(models.Model):
#     name=models.CharField(max_length=50)
#     description=models.TextField()
#     power_level=models.IntegerField()
#     anime=models.ForeignKey(Anime, on_delete=models.CASCADE)


class Swipe(models.Model):
    SWIPE_CHOICES = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    anime=models.ForeignKey(Anime,on_delete=models.CASCADE)
    swipe_type = models.CharField(max_length=10, choices=SWIPE_CHOICES)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} swiped {self.swipe_type} on {self.anime}"


class UserPreference(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    liked_genres = models.TextField(blank=True, default="")
    disliked_genres = models.TextField(blank=True, default="")

    def __str__(self):
        return f"Preferneces for {self.user.username}"

