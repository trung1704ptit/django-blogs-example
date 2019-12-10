from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    # add in thumbail later
    # add in author later

    def __str__(self):
        return self.title