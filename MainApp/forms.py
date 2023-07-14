from django.forms import ModelForm, TextInput, Textarea
from MainApp.models import Snippet
from django.contrib.auth.models import User
from django.forms import CharField, PasswordInput
from django.core.exceptions import ValidationError


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

class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]
    
    password1 = CharField(label = "password", widget = PasswordInput)
    password2 = CharField(label = "password confirm", widget = PasswordInput)

    def clean_password2(self):
        pass1 = self.cleaned_data.get("password1")
        pass2 = self.cleaned_data.get("password2")
        if pass1 and pass2 and pass1 == pass2:
            return pass2
        raise ValidationError("Пароли не совпадают или пустые")
    
    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user