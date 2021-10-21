from django.test import SimpleTestCase
from posts.forms import PostModelForm


class TestForms(SimpleTestCase):

    def test_post_form_valid_data(self):
        form = PostModelForm(data={
            "content": "asdasdasd"
        })
        self.assertTrue(form.is_valid())

    def test_post_form_no_data(self):
        form = PostModelForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
