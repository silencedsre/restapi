from django.db import models

# Create your models here.

class Comment(models.Model):
    author = models.CharField(max_length=150)
    comment = models.TextField(blank=True)
    # image = models.ImageField(upload_to="img/", null=True)

    def __str__(self):
        return self.author