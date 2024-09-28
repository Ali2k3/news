from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Author

class AuthorSignupForm(UserCreationForm):
    email=forms.EmailField(max_length=200,help_text="Required")

    class Meta:
        model=Author
        fields=(
        "username",
        "email",
        "bio",
        "password1",
        "password2")

