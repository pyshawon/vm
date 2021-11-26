from django.contrib import admin
from .models import Vote, VoterArea, Candidate
# Register your models here.


admin.site.register(Vote)
admin.site.register(VoterArea)
admin.site.register(Candidate)
