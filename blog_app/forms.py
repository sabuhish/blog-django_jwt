from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(
        attrs={"class": "form-control"}
    ))
    password2 = forms.CharField(label="Confirm",widget=forms.PasswordInput(
        attrs={"class": "form-control"}
    ))
    class Meta:
        model = User
        fields = (
            "first_name", "last_name", "email"
        )
        labels = {
            "first_name": "Ad",
            "last_name": "Soyad",
            "email": "Email",
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 == password2:
            pass
        else:
            raise forms.ValidationError("Password miss match")