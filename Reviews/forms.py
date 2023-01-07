from django import forms


# One important note , after setting max_length=20 , user not able to write after 20 character 
# and to see the error we have to manually inspect code and from elements section remove max_length arguement 
# to see the error message 
class ReviewForm(forms.Form):
    # error_messages can be editable
    user_name = forms.CharField(label="Your Name",max_length=20, required=True, error_messages= {
        'max_length' : 'Please enter a shorter name',
        'required': 'This field is required', })     # field to show in form
    # addding new fields
    description = forms.CharField(label="Description",widget=forms.Textarea,max_length=200)
    rating = forms.IntegerField(label="Rating",min_value=1,max_value=5)         