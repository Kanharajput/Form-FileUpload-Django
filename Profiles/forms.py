from django import forms

# create a form using django inbuilt forms
class ProfileForm(forms.Form): 
    user_image = forms.FileField(label="")            # file field to take file as input