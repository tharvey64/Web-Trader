from django import forms
from users.models import User

class UserForm(froms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']