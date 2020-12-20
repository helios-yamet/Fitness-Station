from django.test import TestCase
from .forms import ItemForm


def test_item_name_is_required(self):
    form = ItemForm({'name': ''})
    self.assertFalse(form.is_valid())
    self.assertIn('name', form.errors.keys())
    self.assertEqual(form.errors['full_name', 'email', 'phone_number',
                                 'street_address1', 'street_address2',
                                 'town_or_city', 'postcode', 'country',
                                 'county'][0], 'This field is required.')


def test_done_field_is_not_required(self):
    form = ItemForm({'full_name': 'Test checkout Item'})
    self.assertFalse(form.is_valid())


def test_fields_are_explicit_in_form_metaclass(self):
    form = ItemForm()
    self.assertEqual(form.Meta.fields, ['full_name', 'email',
                                            'phone_number',
                                            'street_address1',
                                            'street_address2',
                                            'town_or_city',
                                            'postcode', 'country',
                                            'county'])
