from django.test import TestCase
from products.forms import ProductForm


class TestProductForm(TestCase):
    """
    define product form field requirment,
    self.assertFalse(form.is_valid),
    even if field is empty,
    the add product form is valid.
    If field is required, form will return invalid.
    """

    def test_sku_is_not_required(self):
        form = ProductForm({'name': 'Test Name'
                            'description:' 'Test Description'
                            'price:' '£50.99'})
        self.assertFalse(form.is_valid())

    def test_product_name_is_required(self):
        form = ProductForm({'name': 'Test name'})
        self.assertFalse(form.is_valid())

    def test_description_is_required(self):
        form = ProductForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0],
                         'This field is required.')

    def test_price_is_required(self):
        form = ProductForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')


class TestViews(TestCase):
    """
    Define view products object,
    test response to user request to view products,
    respond with code 200 - server successfully answered the http request
    and fetches the products template.
    """

    def test_view_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
