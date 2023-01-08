from django import forms
from .models import Review

# One important note , after setting max_length=20 , user not able to write after 20 character 
# and to see the error we have to manually inspect code and from elements section remove max_length arguement 
# to see the error message 
'''
class ReviewForm(forms.Form):
    # error_messages can be editable
    user_name = forms.CharField(label="Your Name",max_length=20, required=True, error_messages= {
        'max_length' : 'Please enter a shorter name',
        'required': 'This field is required', })     # field to show in form
    # addding new fields
    description = forms.CharField(label="Description",widget=forms.Textarea,max_length=200)
    rating = forms.IntegerField(label="Rating",min_value=1,max_value=5)         
'''

# creating a form using model 
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review                # model using which we have to create the form 
        # here we want to use all columns as fields
        fields = '__all__'            # name the columns which can be used as fields
        # if there are some columns which we don't want use as fields
        # column name passed in execule execuled from form other fields automatically added
        # exclude = ['']              
        labels = {
            "username": "Your Name",
            "desription":"Description",
            "rating": "Your rating"
        }

        error_messages = {
            "username":{
                "required":"Your name must not be empty",
                "max_length":"Enter a short name"
            }
        }
