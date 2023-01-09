from django import forms

# create a form using django inbuilt forms
class ProfileForm(forms.Form): 
    user_image = forms.ImageField(label="")            # now it only accept the images