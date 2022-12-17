from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        USER, on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    category = models.CharField(max_length=100, default="TBD")
    story_image = models.URLField(max_length=500, default="https://via.placeholder.com/150")
    class Meta:
        ordering = ['-pub_date']

    

 