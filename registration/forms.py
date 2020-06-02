from django import forms


class usernameForm(forms.Form):
    username = forms.CharField(label="", min_length=1, max_length=20,
                               widget=forms.TextInput(attrs={"placeholder":"Username","style":"font-size: x-large"}))


class passwordForm(forms.Form):
    password = forms.CharField(label="",min_length=6, max_length=20 ,widget=forms.PasswordInput(attrs={
    'class': 'input-text with-border', 'placeholder': 'Password',"style":"font-size: x-large"}))


class repeatPasswordForm(forms.Form):
    repeatPassword = forms.CharField(label="", min_length=1, widget=forms.PasswordInput(attrs={
    'class': 'input-text with-border', 'placeholder': 'Repeat password',"style":"font-size: x-large"}))