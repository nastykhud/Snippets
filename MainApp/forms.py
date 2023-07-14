from django.forms import ModelForm, TextInput, Textarea
from MainApp.models import Snippet


class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code', 'public']
       labels = {'name': 'Имя', 'lang': 'Язык', 'code': 'Код', 'public': 'Публичный'} #это лейбл перед эдитом
       widgets = {
           'name': TextInput(attrs = {'placeholder': 'Название сниппета'}), #это подсказки внутри эдитов
           'code': Textarea(attrs = {'placeholder': 'Код сниппета'})
       }
#Так можно указать поля, которые нужно исключить (нельзя использовать вместе с fields)
# exclude = ['lang']