from django.db import models

class Search(models.Model):
    search_text = models.CharField(max_length=200)

    def __str__(self):
        return self.search_text