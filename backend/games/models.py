from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    ) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review of {self.user_name} for {self.game.title}'
    
    class Meta:

        ordering = ['-created']

