from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Candidate(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class VoterArea(models.Model):
    name = models.CharField(max_length=20)
    total_voter = models.PositiveIntegerField(default=0)
    candidates = models.ManyToManyField(Candidate, blank=True)

    def __str__(self):
        return self.name


class Vote(models.Model):
    title = models.CharField(max_length=20)
    area = models.ForeignKey(VoterArea, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        super(Vote, self).save(*args, **kwargs)


class VoteResult(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    vote_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.vote.title
