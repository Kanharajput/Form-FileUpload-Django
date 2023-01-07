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