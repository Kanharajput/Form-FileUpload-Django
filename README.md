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
    - 5. Using CreateView        -> it automatically save the data
    - As you go from 1 to 4 each time the django tries to less the code we write, and add some advance functionaly.

CREATE SIMPLE TAKE MODEL AND CREATE A BRAND NEW FORM WITHOUT THE NEED OF FORM MODELFORM OR FORM CLASS
- But one can pass the ModelForm class as in CreateView we can not write label and error messages 



"# File uploads in django" 
AFTER THIS COMMIT WE ARE WORKING ON FILE UPLOADS

DATABASES NEVER STORE THE FILES
- They actually store the file somewhere else and only store the address of that file, to access it later
- because if we store the file then it lower down the speed of database. NOw you are thinking then where it stores the files? 
- Django store the files on the base folder of os that's user/user-name of pc , but it's not a good idea to store a project files outside of the project folder, so Django provide MEDIA_ROOT , ANY path passed in MEDIA_ROOT will be concluded by django as base folder path to store the files.
- Rememeber on server also there is os running, so it also possible there, don't be confused like how server have an os or folder and all things but server have all this things.
- This same concept is also used when we save a file using admin panel that file also saves like this.

TO WORK WITH IMAGES WITH HAVE TO INSTALL PILLOW 
- command : pip install Pillow


TO SERVE MEDIA FILES WE NEED TO ADD MEDIA_URL
- MEDIA_URL is url which is used by django to serve the MEDIA_ROOT files there , so that a user can't directyly access the MEDIA_ROOT folder as it is in base directory , so it is not a good option according to security reasons. 
- MEDIA_URL is just a url which is not seen by the developers and not by the users it is run behind the scene and let the browser security access the MEDIA_ROOT files.
- Also we have to add this MEDIA_ROOT and MEDIA_URL in project level static files.


"# Sessions in Django" 
- Sessions let us the save the data which is specific for a user for a fixed period of time.
- Server have a session identifier and that session identifier is also passed to browser in a cookie through which server identifies an user and can return related preferences/data to that user.
- This session data is stored in a database or may be in a file.
- Session not able to store objects, one can store boolean values, numbers , string and even dictionary but not the objects. Under the hood Django takes the session data and covert it into json format, and the objects are eligible to be formated as json. so simply store numbers , strings, dictionary and boolean values.