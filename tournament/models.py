from django.db import models
from django.utils import timezone

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=256,)
    image = models.ImageField(null=True)

    def __unicode__(self):
        return self.name

    
class Tournament(models.Model):
    name = models.CharField(max_length=256)
    players = models.ManyToManyField(Player)
    player_max = models.IntegerField()
    current = models.BooleanField(default=False)
    start = models.DateTimeField()

    def __unicode__(self):
        return self.name


class Match(models.Model):
    tournament = models.ForeignKey(Tournament)
    player_one = models.ForeignKey(Player, related_name='player_one')
    player_two = models.ForeignKey(Player, related_name='player_two')
    winner = models.ForeignKey(Player, related_name='winner')
    start = models.DateTimeField(blank=True, null=True)
    verbose_name_plural = 'Matches'

    def __unicode__(self):
        return self.tournament.name + " " + str(self.start)

    class Meta:
        verbose_name_plural = 'matches'
    

    
