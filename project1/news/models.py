from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=90)
    body = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


