"# FormInDjango" 

FORM METHODS:
- form has by default GET method to submit data
    - GET method is used to get the data from the server and create an url e.g. http://localhost:8000/?username=kanha , here username is the field and kanha is the data passed in the field. It also create key value but that is passed with Query String Parameter

    - POST method is used to send the data to the server and it don't attach field and it's data to the url rather then this key-value pair is passed in the form data, check this difference through network panel provided in developer tools window.

CSRF Token:
- CSRF stands for Cross Site Request Forgery.
    - This token is used to check the request is coming from a valid source.
    - Scenario : Let say, a Bank site is forged by someone and forged site is looked very similar to actual site and also it's url is very much similar. Then a customer comes to the site and send money to his friend using that forged site till this all work fine but after this, the people who forged the site change the recepient account no with him  in the request and server also don't identified this and the transaction successed. 
    - This fraud can be protected by csrf token. How ? Server generate a token automatically and put it with the form, now after submiting the form, server check the request, if the token is found then only it pass the request otherwise the operation is failed.
    - In the whole scenario we have only one server but two site one is real and one is fake so csrf token let the server identify that from which site the request is coming.


MANUALLY REVIEW THE FORM DATA:
- we can manually valide the form data, but it not make any sense. For different forms in different template we have to do the same work again and again.
- Django provide Form class to work with form and validate them also.


WHEN ERRORS OCCURS:
- Actually this errors will never gonna occur because if we set a field then django will let us submit the form with an empty value and it will never reach to the server 
- Here django will by default set the field required=True, so we will never going to see that error message when the field is empty. 
- But using a trick we see it we go to the inspect of the page change the source and then make that required=False and now we can submit the form and see the error
- Which is not possible for an user why an user will do such thing it is the course that's why I am doing it otherwise it is not making any sense to me.

STYLING ELEMENTS WHICH ARE PROVIDED BY DJANGO IN FORM
- Those elements also a id to see their id visit the page which we want to style
- Inspect the page and then open the Elements window and check the html code 
- That code consist the html code of the elements injected by django , they also have id
- We can use that id to style the elements


FORM RENDERING METHODS 
- In this project only we see 4 ways to render and handle the form
    - 1. Using normal view function.  ->  check code in previous commit deleted for now
    - 2. Using Form class
    - 3. Using ModelForm class 
    - 4. Using FormView

    - As you go from 1 to 4 each time the django tries to less the code we write, and add some advance functionaly.
