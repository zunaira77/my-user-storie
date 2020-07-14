from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):

    einfach = 'Niveau: Einfach'
    mittel = 'Niveau: Mittel'
    schwer = 'Niveau: Schwer'

    NIVEAU_CHOICES = [
        (einfach, 'Niveau: Einfach'),
        (mittel, 'Niveau: Mittel'),
        (schwer, 'Niveau: Schwer'),
    ]
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    teaser = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    niveau = models.CharField(
        max_length=200,
        choices=NIVEAU_CHOICES,
        blank=True,
    )
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    cover = models.ImageField(upload_to='media/images/', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title