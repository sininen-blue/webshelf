from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length="32")
    password = forms.CharField(label="password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label="username", max_length="32")
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        label="confirm password", widget=forms.PasswordInput
    )
