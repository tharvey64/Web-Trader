from django import forms
# from users.models import User

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['amount', 'account_number']