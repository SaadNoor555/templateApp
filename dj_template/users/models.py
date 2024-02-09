from django.db import models

class Writer(models.Model):
    id      = models.AutoField(primary_key=True)
    name    = models.CharField(max_length=50)
    birth   = models.DateTimeField()
    age     = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f'{self.name} was born in {self.birth}. He has authored many books'


class Book(models.Model):
    author  = models.ForeignKey(Writer, related_name='author', on_delete=models.CASCADE)
    id      = models.AutoField(primary_key=True)
    name    = models.CharField(max_length=50)
    genre   = models.CharField(max_length=15)
    

    def __str__(self) -> str:
        return f'{self.name} is a famous {self.genre} book by {self.author.name}'
