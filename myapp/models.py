from django.db import models

class Influencer(models.Model):
    handle = models.CharField(max_length=400)
    name = models.CharField(max_length=400)
    followers = models.CharField(max_length=400)
    likes = models.CharField(max_length=400)
    profile_picture = models.CharField(max_length=400)

    def __str__(self):
        return self.handle
    
    def message(self):
        return f'Hello from {self.name}'