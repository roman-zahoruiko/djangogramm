from django.test import SimpleTestCase
from profiles.forms import ProfileModelForm


class TestForms(SimpleTestCase):

    def test_profile_form_valid_data(self):
        form = ProfileModelForm(data={
            "first_name": "123",
            "last_name": "123",
            "bio": "321",
            "country": "111",
            "avatar": "url",
        })
        self.assertTrue(form.is_valid())

    def test_profile_form_no_data(self):
        form = ProfileModelForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
