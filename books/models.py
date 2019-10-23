from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title