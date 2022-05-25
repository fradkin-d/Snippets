from django.forms import ModelForm, TextInput, Textarea, CharField, PasswordInput, ValidationError
from MainApp.models import Snippet
from django.contrib.auth.models import User


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ['name', 'lang', 'code']
        widgets = {
            'name': TextInput(attrs={"class": "form-control form-control-lg", 'placeholder': 'Название сниппета'}),
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
