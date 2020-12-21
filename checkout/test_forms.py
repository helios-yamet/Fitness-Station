from django.test import TestCase
from checkout.forms import MakePaymentForm
from django.contrib.auth.models import User
from django.core.management import call_command
from datetime import datetime
from fitness_station.settings import STRIPE_SECRET_KEY


class TestMakePaymentForm(TestCase):
    """
    Test MakePayment Form
    """

    @classmethod
    def setUpTestData(self):
        # set up db, order matters because of Many to Many Relationships

        # set up 3 base products from json
        call_command('loaddata',
                     'products/fixtures/servicelevel.json', verbosity=0)

        # create users
        user = User(
            username='testing_{1',
            email='testing_1@test.com',
            password='Tester_1234!'
        )
        user.save()
        self.user = user
        self.year = int(datetime.now().strftime("%Y")) + 1
        self.month = int(datetime.now().strftime("%m"))

    def test_make_payment_form_success(self):
        form = MakePaymentForm({
            'credit_card_number': '4242424242424242',
            'ccv': 'test_user1',
            'expiry_month': self.month,
            'expiry_year':  self.year,
            'stripe_id': STRIPE_SECRET_KEY,
        })
        self.assertTrue(form.is_valid())

    def test_make_payment_form_invalid(self):
        form = MakePaymentForm({
            'credit_card_number': '4242424242424242',
            'ccv': 'test_user1',
            'expiry_month': self.month,
            'expiry_year': self.year,
        })
        self.assertFalse(form.is_valid())
