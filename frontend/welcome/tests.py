from django.core.urlresolvers import reverse
from django.test import TestCase

from . import forms


class FormTests(TestCase):
    def test_superuser_creation(self):
        form = forms.CreateFirstSuperUser({
            'username': 'admin',
            'email': 'ava_first_admin@avasecure.com',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertTrue(form.is_valid())

        user = form.save()
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.rights.is_admin)

    def test_users_already_exist(self):
        """Form validation fails if any users already exist."""
        form = forms.CreateFirstSuperUser({
            'username': 'admin',
            'email': 'ava_first_admin@avasecure.com',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertTrue(form.is_valid())
        form.save()

        form = forms.CreateFirstSuperUser({
            'username': 'another_admin',
            'email': 'ava_second_admin@avasecure.com',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertFalse(form.is_valid())


class ViewTests(TestCase):
    def test_user_creation_and_login(self):
        """Test the first-user flow."""
        # Post a valid form to the user creation and follow
        # the redirects. By the time we get to the end of the
        # chain we should be at 'success_url' and logged in as
        # the user we just created.
        response = self.client.post(
            reverse('welcome-first-user'),
            data={
                'username': 'admin',
                'password1': 'password',
                'password2': 'password'
            },
            follow=True)
        # Check we're magically logged in as 'admin'
        user = response.context['user']
        self.assertEqual(user.username, 'admin')
