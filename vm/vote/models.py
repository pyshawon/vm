from django.db import models

# Create your models here.


class VoterArea(models.Model):
    name = models.CharField(max_length=20)
    total_voter = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=30)
    area = models.ForeignKey(VoterArea, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Vote(models.Model):
    title = models.CharField(max_length=20)
    area = models.ForeignKey(VoterArea, on_delete=models.CASCADE)
    vote_by = models.ManyToManyField('account.Profile', blank=True)

    def __str__(self):
        return self.title
