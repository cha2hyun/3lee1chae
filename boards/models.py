from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos')
    text = models.TextField()
    date = models.DateField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return f'{self.author.username}'

    def get_absolute_url(self):
        return reverse('board:board_detail', args=[str(self.id)])
