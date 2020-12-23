from django.test import TestCase
from review.forms import ReviewForm


class TestReviewForm(TestCase):

    def test_name_is_required(self):
        form = ReviewForm({'name': 'Test name'})
        self.assertFalse(form.is_valid())

    def test_review_text_is_required(self):
        form = ReviewForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('review_text', form.errors.keys())
        self.assertEqual(form.errors['review_text'][0],
                         'This field is required.')
