from django.db import models
from django.contrib.auth.models import User

LANGS = (
    ('py', 'Python'),
    ('js','JavaScript'),
    ('cpp', 'C++')
)

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices = LANGS)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to = User, on_delete = models.CASCADE, blank = True, null = True)
    public = models.BooleanField(default = True) #True - public, False - private

    def __str__(self):
        return f'{self.__class__.__name__}{self.name, self.lang}'
