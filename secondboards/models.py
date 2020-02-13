from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Board(models.Model):
    authors = models.ForeignKey(
        User, related_name='second', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='buyphotos')
    text = models.TextField()
    date = models.DateField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return f'{self.authors.username}'

    def get_absolute_url(self):
        return reverse('secondboard:board_detail', args=[str(self.id)])
