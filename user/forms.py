from django import forms

class LoginForm(forms.Form):
     username = forms.CharField(max_length=25, min_length=5, label="username")
     password = forms.CharField(max_length=20, min_length=8, widget=forms.PasswordInput)



class RegisterForm(forms.Form):
     username = forms.CharField(max_length=50, min_length=5, label="Username")
     password = forms.CharField(max_length=20, min_length=5, label="Password", widget= forms.PasswordInput)
     confirm = forms.CharField(max_length=20, min_length=5, label="Confirm Password", widget= forms.PasswordInput)


     def clean(self):
          username = self.cleaned_data.get("username")
          password = self.cleaned_data.get("password")
          confirm = self.cleaned_data.get("confirm")

          if password and confirm and password != confirm:
               raise  forms.ValidationError("Passwords doesn't match!")

          values = {
               "username": username,
               "password": password
          }
          return  values

