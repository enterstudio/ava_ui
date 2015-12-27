from ava.core_auth.models import UserRights

from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import fields, widgets


# from builtins import False


class UserForm(ModelForm):
    # Fields related to user rights.
    is_admin = fields.BooleanField(label='System Administrator', required=False)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # If there's an existing user, set the initial state of the user rights.
        if self.instance and self.instance.id:
            user_rights = UserRights.get(self.instance)
            self.initial.update({
                'is_admin': user_rights.is_admin,
            })

    def save(self, *args, **kwargs):
        user = self.save_user(*args, **kwargs)
        self.save_user_rights(user)
        return user

    def save_user(self, *args, **kwargs):
        return super(UserForm, self).save(*args, **kwargs)

    def save_user_rights(self, user):
        user_rights = UserRights.objects.get_or_create(user=user)[0]
        user_rights.is_admin = self.is_checkbox_set('is_admin')
        user_rights.save()

    def is_checkbox_set(self, name):
        if name not in self.cleaned_data:
            return False
        return True if self.cleaned_data[name] else False


class UserCreateForm(UserForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'first_name', 'last_name', 'email', 'is_admin', 'is_active']

    password = fields.CharField(widget=widgets.PasswordInput, label='Password', required=True)
    password2 = fields.CharField(widget=widgets.PasswordInput, label='Confirm password', required=True)

    def clean(self):
        cleaned_data = super(UserCreateForm, self).clean()
        if cleaned_data.get('password') != cleaned_data.get('password2'):
            self.add_error('password2', 'The passwords entered do not match')

    def save_user(self, *args, **kwargs):
        user = super(UserCreateForm, self).save_user(*args, **kwargs)
        # The user needs to be saved again after their password is set.
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user


class UserUpdateForm(UserForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_admin', 'is_active']
