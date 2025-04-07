from django.db import models
from django.contrib.auth.models import User

class Anime(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    genres=models.CharField(max_length=255)

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

