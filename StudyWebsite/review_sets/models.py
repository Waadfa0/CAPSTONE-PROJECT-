from django.db import models
from django.contrib.auth.models import User
from main.models import StudyGroup

# Create your models here.

class ReviewSet(models.Model):
    title = models.CharField(max_length=2000)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    group=models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    
    #string representation
    def __str__(self):
        return self.title

# ناقصني السيت اي دي خلاني ابكي 

class FlashCard(models.Model):
    review_set = models.ForeignKey(ReviewSet, on_delete=models.CASCADE)
    question = models.CharField(max_length=2000)
    answer = models.CharField(max_length=2000)
