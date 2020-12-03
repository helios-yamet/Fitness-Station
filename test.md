# Testing


## Contents
* [Responsiveness](#Responsiveness)
     * [Browsers](#Browsers)
     * [Phones](#Phones)
     * [Tablets](#Tablets)
     * [Laptops](#Laptops)
* [Site-Performance-testing](#Site-Performance-Testing)
     * [Testing-mobile-friendliness](#Testing-Mobile-Friendliness)
     * [Functional-testing](#Functional-Testing)
* [Code-validity](#Code-Validity)
     * [HTML](#HTML)
     * [CSS-Code-Test](#CSS-Code-Test)
     * [JavaScript-Code-Test](#JavaScript-Code-Test)
     * [Python-Code-Test](#Python-Code-Test)
* [issues-and-bugs](#issues-and-bugs)
     * [#](#)
* [Django-testing](#Django-Testing)
     * [Allauth-authentication](Allauth-Authentication)
* [Stripe-Testing](#Stripe-Testing)
     * [#](#)

## Responsiveness

### Browsers

* The Chrome and Firefox browser development tools were used to check for responsiveness and scaling issues on different screen sizes.

* This project was tested across multiple browsers (Chrome, Opera, Safari, Firefox, and IE) in different simulated and real devices.

### Phones

  - Galaxy Note 8
  - Galaxy Note 9
  - Gakaxy Note 10 (real device)
  - Galaxy S5
  - Galaxy S7+ (real device)
  - Galaxy S9/S9+ (real device)
  - Galaxy S10 (real device)
  - iPhone 5/SE
  - iPhone 6/7/8
  - iPhone 8 Plus (real device)
  - iPhone X (real device)
  - iPhone XR (real device)
  - iphone XS 
  - iphone XS Max (real device)
  - Huawei P30 Pro (real device)
  - Nexus 5X
  - Nexus 6P
  - Pixel 2
  - Pixel 2 XL

### Tablets
  - iPad (real device)
  - iPad Pro 10.5-inch
  - iPad Pro 12.9
  - Kindle Fire HDX
  - Nexus 10
  - Nexus 7

### Laptops

  - MacBook Pro 13" (real device)
  - Asus Swift 3 (real device)

* Windows 10 computer
  - Philips 1080p Full HD (real device)
 
**Were found some display issues with discontinued browsers such as IE and obsolete versions of Chrome and Opera.**

## Site performance testing

### Testing mobile friendliness
*Applied the google lighthouse tool and mobiReady online automated tools:*

#### Google developer tool lighthouse:
   - Opened Google developer tools on-site, find lighthouse on navigation bar(next to security) and click generate report.
   
Results below:

  <details>
  <summary>Lighthouse</summary>
  <br>
  <div align="center">
    <img src="https://github.com/michodgs25/Sprint/blob/master/static/images/test-results/lighthouse-results.jpg"
         </div>
    </details>

----

#### mobiReady mobile test:
  - Enter website link as indicated into enter bar on homepage, press enter and the site automates the website to whether it will be mobile ready.
  
  <details>
  <summary>MobiReady</summary>
  <br>
  <div align="center">
    <img src="https://github.com/michodgs25/Sprint/blob/master/static/images/test-results/mobi-test.jpg"
         </div>
    </details>


* *Both tests come back positive with only minor errors.*

----

## Functional testing 
To ensure each feature works as intended, I manually tested each platform feature welcome page, to the footer icon links:
 
 
 __Welcome page__ - button lights up, transports me to the homepage as expected and image and texts are all as intended.
 
 __Home page__ - Both card buttons light up and transport me to the correct pages. Card images and texts all as intended.
 
 __Create Sprint page__ - The navigation bar which is fixed(follows user scroll) links, works as intended, the JS function successfully hid the search bar
 (Ensuring the user explores the sprint on the explore sprints page only),
each text input, textarea and select allowed me to input the information and when redirected, that information had been saved correctly. In addition the footer links work also as intended. 

The create page sidenav also works as intended functionally and stylistically with each link taking the user to each respective page.
The search text input is also hidden successfully as intended.
 
__Explore Sprints page__ - Like the create page, the navigation bar which is fixed(follows user scroll) the bar links, search text input and reset button works as intended. Searching sprint logs returned the desired data and returned no logs if data inputted did not exist within the database. Each accordian has the intended header texts and body has the title& description of each individual log.

The explore page sidenav like the desktop navigation, the links and search text input plus reset button all work as intended. 

__Error page__ - page image and button works as intended with the latter taking the user back to the homepage.
 
 ----

## Code validity

### Testing Code validity - iiii.
Tested html and css code formatting with https://validator.w3.org/ - done by copying& pasting the code via direct input into the site text box. 

Tested the JavaScript code with https://jshint.com/ - done by copying& pasting the code via direct imput into the site text-area. 

Tested the Python code with http://pep8online.com/ - done by copying& pasting the code via direct imput into the site text-area.

### Validators Summary

#### HTML

  - [The W3C Markup Validation Service](https://validator.w3.org/)
  
  * Goal - to achieve error free html.

* A handful of errors found via base.html(bulk of html code):

the {{url_for('') }} jinja method used frequently throughout the project as this provided easy access to each page of the platform for the user calling each page from the app.py file. This was not changed as the benefits outweighed the negatives plus both my mentor course institute informed me that I can ignore those errors.

The other errors that I was unable to resolve were using form& div tags as a descendant of a ul tag which can only have li tags as descendants of the ul tag:

* div tag error 
```
<ul id="mobile-demo" class="sidenav light-blue darken-4">
                <div class="user-view">
                    <div class="background">
                        <!--Sprint title& image, increase user interaction-->
                        <img src="{{url_for('static', filename='images/website/sidenav-image.jpg')}}" alt="Male athlete in running motion">
                    </div>
                    <h6 class="side-title">Sprint</h6>
                </div>`
                
```

These minor errors do not adhere to software development standards but the design and functionality of the sidenav fit the vision of the site whereas replacing the tags made the image, tabs, and search bar untidy.

For the other Html templates: index.html, home.html, add_activity.html error.html, edit_activity.html and explore.html. Barring the jinja template code, all came back error free. Goal partially achieved.

#### CSS Code Test

* *Goal - to ensure CSS is error free*

  - [The W3C Markup Validation Service](https://jigsaw.w3.org/css-validator)
  
<details>
  <summary>CSS test</summary>
  <br>
<div align="center">
<img src="https://github.com/michodgs25/Sprint/blob/master/static/images/test-results/css-test.jpg" target="_blank" rel=""/>
</div>
  </details>

* No errors found, goal achieved.

------

#### JavaScript Code Test

  - [JS Hint](https://jshint.com/)
  
 <details>
  <summary>JS-hint test</summary>
  <br>
<div align="center">
<img src="https://github.com/michodgs25/Sprint/blob/master/static/images/test-results/js-test.jpg" target="_blank" rel=""/>
</div>
  </details>

*  Two undefined variable which is the dollar sign, this js code was adapted from materialize js, future iterations to explore this. 
However No errors found, goal achieved.

#### Python Code Test

* *Goal to ensure python code has no errors*

 - PEP8 (http://pep8online.com/)
 
 <details>
  <summary>Pep8 test</summary>
  <br>
<div align="center">
<img src="https://github.com/michodgs25/Sprint/blob/master/static/images/test-results/pep-test.png" target="_blank" rel=""/>
</div>
  </details>
 
 * No errors found, goal achieved.

---- 

## Django local tests

Using django testing immediately after installing and implementing django applications.

#### Allauth-authentication

By default django sends confirmation emails to any new accounts, at the beginning of the project I temporarily made those confirmations be sent to the console; did this by adding these in settings.py:  
```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' - Tells allauth that we want to allow authentication using either usernames or emails.
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'  - Ensures an email is required to register to the site.
ACCOUNT_EMAIL_REQUIRED = True - Ensures an email is required to register to the site.
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' - Ensures an email is required to register to the site.
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True - Ask user to enter password twice, avoid any typos.
ACCOUNT_USERNAME_MIN_LENGTH = 4 - Required length of a username.
LOGIN_URL = '/accounts/login/' - login url.
LOGIN_REDIRECT_URL = '/success' - Url to redirect to, once logged in.
```

* In order to test whether allauth is working properly, I will run the server with python3 manage.py runserver and open project. 

* Then I navigate to the login page and try to sign in using my superuser username& password. 

* Once entered those details, it redirected me back to a verify your email page, this indicates that allauth is working as expected, because email confirmations are now required in order to log in. *Caution, however I created the user before installing allauth, I resolved this by adding the username and password to the email addresses in admin/accounts/email addresses, and clicking both primary and verified boxes.*

* I logged out and tried again to login, this time I got a 404 page with the  request message: "//localhost:8000/success", this means that the authentication works as we have been redirected to the /success url we set which confirms authentication is working. 

* After authentication test is over I change the redirect url from /success to '/' in settings.py.

#### Stripe Testing

*Stripe provide a number of tests that ensure card information cannot be duplicated, outright stolen or if incorrect information is inputted*

* To test Stripe card payments I used the Stripe testing documentation: https://stripe.com/docs/testing

To test whether submitting order works as expected
