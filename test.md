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
* [Django-local-tests](#Django-Local-Tests)
     * [Checkout-form-tests](#Checkout-Form-Tests)
     * [Test-products-review-form](#Test-Products-Review-Form)
     * [Allauth-authentication](Allauth-Authentication)
* [Stripe-Testing](#Stripe-Testing)
* [Automated-local-testing](#Automated-Local-Testing)

---------------------


## Responsiveness

### Browsers

* The Chrome and Firefox browser development tools were used to check for responsiveness and scaling issues on different screen sizes.

* This project was tested across multiple different browsers (Chrome, Opera, Safari, Firefox) in different simulated and real devices.

### Phones

  - Gakaxy Note 10 (real device)
  - Galaxy S10 (real device)
  - iPhone 5/SE
  - iPhone 6/7/8
  - iPhone 8 Plus (real device)
  - iPhone X (real device)
  - iPhone XR (real device)
  - iphone XS 
  - iphone XS Max (real device)
  - Huawei P30 Pro (real device)
  - Pixel 2
  - Pixel 2 XL

### Tablets
  - iPad (real device)
  - iPad Pro 10.5-inch
  - iPad Pro 12.9
  - Kindle Fire HDX
  - Nexus 10

### Laptops

  - MacBook Pro 13" (real device)
  - Asus Swift 3 (real device)

* Windows 10 computer
  - Philips 1080p Full HD (real device)
  - Lenovo ThinkPad
 
----------------------

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
    <img src="https://github.com/michodgs25/Fitness-Station-360/blob/master/media/readme/fitness-lighthouse.png"
         </div>
    </details>
    
 * *Lighthouse result solid to positive test results.

----

#### mobiReady mobile test:
  - Enter website link as indicated into enter bar on homepage, press enter and the site automates the website to whether it will be mobile ready.
  
  <details>
  <summary>MobiReady</summary>
  <br>
  <div align="center">
    <img src="https://github.com/michodgs25/Fitness-Station-360/blob/master/media/readme/fitness-mobi-ready.png"
         </div>
    </details>


* *Both tests come back positive with only minor errors.*

----

## Functional testing 
To ensure each feature works as intended, I manually tested each platform feature homepage, to the footer cards:
 
 
 __Home page__ -
 
__Products Page__ - 

__Product Review page__ -

__Bag page__ - 

__Checkout page__ - 

__Checkout success page__ - 

__Contact page__ - 

__Profile page__ -

__Past order__ -
 
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

* A handful of errors found primarily jinja syntax

the {{url_for('') }} jinja method used frequently throughout the project as this provided easy access to each page of the platform for the user to request each page. This was not changed as the benefits outweighed the negatives plus both my mentor course institute informed me that I can ignore those errors. 
Also special values like += are also deemed errors but can be ignored.

For the other Html templates barring the jinja template code, all came back error free. Goal partially achieved.

#### CSS Code Test

* *Goal - to ensure CSS is error free*

  - [The W3C Markup Validation Service](https://jigsaw.w3.org/css-validator)

<details>
  <summary>Base, Profile and Checkout Css</summary>
  <br>
<div align="center">
<img src="https://github.com/michodgs25/Fitness-Station-360/blob/master/media/readme/css-validate.png" target="_blank" rel=""/>
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
<img src="" target="_blank" rel=""/>
</div>
  </details>

*  .

#### Python Code Test

* *Goal to ensure python code has no errors*

 - PEP8 (http://pep8online.com/)
 
 <details>
  <summary>Pep8 test</summary>
  <br>
<div align="center">
<img src="https://github.com/michodgs25/Fitness-Station-360/blob/master/media/readme/pep8.png" target="_blank" rel=""/>
</div>
  </details>
 
 * No errors apart from a few lines that are two long but cutting them, negatively affected the other code, so left alone.

---- 

## Django local tests

Using django testing immediately after installing and implementing django applications.

#### Checkout form tests

I ran 'python3 manage.py test' in my gitpod terminal to run all tests(6), the purpose of this test is to automate filling out the checkout form, and returning each field.
Results came back successful 'OK'

See checkout test code below:

```
from django.test import TestCase                 
from checkout.forms import OrderForm 


class TestOrderForm(TestCase):

    def test_full_name_is_required(self):
        form = OrderForm({'full_name': 'Test name'})
        self.assertFalse(form.is_valid())

    def test_email_address_is_required(self):
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_street_address1_is_required(self):
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1'][0],
                         'This field is required.')

    def test_street_address2_is_not_required(self):
        form = OrderForm({'full_name': 'Test Name'
                          'email:' 'Test Description'
                          'street_address1:' 'Test Address'
                          'town_or_city:' 'Test Town or City'
                          'postcode:' 'Test Postcode'
                          'phone_number:' 'Phone Number'})
        self.assertFalse(form.is_valid())

    def test_town_or_city_is_required(self):
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0],
                         'This field is required.')
                         
    def test_phone_number_is_required(self):
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0],
                         'This field is required.')

```

See additional automated testing issues below:

#### Test products review form:

https://github.com/michodgs25/Fitness-Station-360/issues/9#issue-773380139


#### Test add products form: 

https://github.com/michodgs25/Fitness-Station-360/issues/8#issue-773365697

------------

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

#### User Authentication error and resolution

I deployed the platform and sent it to my friends for testing, an immediate issue came up, user would register an account, confirmation link recieved and is clicked, the user is then taken back to the verify email page(not logged in) and another link sent to the user address.

The reason for this issue, was never discovered during a prolonged investigation period, but a resolution/compromise was found:

```
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_EMAIL_VERIFICATION = None
```
the above code is placed below:

```
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
```
in settings.py

this essentially bypasses the need for the user to verify their email address by going to their email account.

Valid email and password safeguards to ensure platform safety....

## Stripe Testing

*Stripe provide a number of tests that ensure card information cannot be duplicated, outright stolen or if incorrect information is inputted*

* To test Stripe card payments I used the Stripe testing documentation: https://stripe.com/docs/testing

* To check whether an order exist or not, I applied two pieces of code taken from the code institute Boutique Ado project -  https://github.com/ckz8780/boutique_ado_v1/blob/a07c1ca5a3b973eb47e5c944829cea06ead3936d/checkout/static/checkout/js/stripe_elements.js 
   first assuming that an order has not been placed:
```
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
* 
```
```
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)
```
And the second assumming that an order has been placed, responding with a success webhook and send the confirmation to the user. 
However if there is no order, attempt create it using the json version in payment intent and if anything does go wrong(user loses wifi connection for example),
the order will be deleted. 
This prevents any unauthorised orders and protects the customer.

To prevent potential processes being slower than other thereby causing a potential error, again I applied a delay code mechanism taken from project boutique Ado:
https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/90cda137ebaa461894ba8c89cd83291a/?activate_block_id=block-v1%3ACodeInstitute%2BFSF_102%2BQ1_2020%2Btype%40sequential%2Bblock%4090cda137ebaa461894ba8c89cd83291a

For orders not found immediately, for each second out of five total seconds, the webhook handler attempts to find the order five different times.

```
attempt = 1
while attempt <= 5:
```

To test the above functionality, I made test order using a test card number 
- 4242 4242 4242 4242
- month(any)
- CVC(any)
- zip(any)

taken from stripe testing documents: https://stripe.com/docs/testing 
and then check the stripe webhook response: 
