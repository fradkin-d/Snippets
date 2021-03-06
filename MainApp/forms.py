from django.forms import ModelForm, TextInput, Select, Textarea, CheckboxInput, CharField, PasswordInput, ValidationError
from MainApp.models import Snippet, Comment
from django.contrib.auth.models import User


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ['name', 'lang', 'code', 'is_public']
        widgets = {
            'name': TextInput(attrs={"class": "form-control form-control-lg",
                                     'placeholder': 'Дайте имя сниппету ...'}),
            'lang': Select(attrs={"class": "form-control form-control-lg"}),
            'code': Textarea(attrs={"class": "form-control form-control-lg", 'placeholder': 'Поместите код сюда ...'}),
        }


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

    password1 = CharField(label="Password", widget=PasswordInput)
    password2 = CharField(label="Password confirm", widget=PasswordInput)

    def clean_password2(self):
        pass1 = self.cleaned_data.get("password1")
        pass2 = self.cleaned_data.get("password2")
        if pass1 and pass2 and pass1 == pass2:
            return pass2
        raise ValidationError("Пароли не совпадают или пустые")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': TextInput(attrs={"class": "form-control form-control-lg",
                                     'placeholder': 'Ваш комментарий ...'})
        }
