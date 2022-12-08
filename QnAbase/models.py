from django.db import models
from django.contrib.auth.models import User,AbstractUser

# class CustomUser(AbstractUser):
#     bio=models.TextField()
#     location=models.CharField(max_length=200)

# question model
class Question(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    # detail = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
#Answer Model
class Answer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    detail = models.TextField(default=' ')
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail
    
class Comment(models.Model):
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    comment = models.TextField(default=' ')
    add_time = models.DateTimeField(auto_now_add=True)

class Upvote(models.Model):
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='upvote')
    
class Downvote(models.Model):
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='downvote')
    