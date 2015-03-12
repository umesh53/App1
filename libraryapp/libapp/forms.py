from __future__ import unicode_literals

import warnings

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from models import BookUserMap
from models import Books
from django.contrib.auth import authenticate, get_user_model


class LoginForm(forms.Form):
        username        = forms.CharField(label=(u'User Name'))
        password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))


class BookForm(ModelForm):
        bd_id = forms.IntegerField(widget=forms.HiddenInput(),required=False)

        # def clean_model_instance(self):
        #         da_id = self.cleaned_data['bd_id']
        #         if not da_id:
        #                 raise forms.ValidationError()
        #         try:
        #                 instance = BookForm.objects.get(id=da_id)
        #         except BookForm.DoesNotExist:
        #                 raise forms.DoesNotExist()
        #         return instance
        def save(self, force_insert=False, force_update=False, commit=True):
            m = super(BookForm, self).save(commit=False)
            try:
                book = Books.objects.get(id = self.cleaned_data['bd_id'])
            except:
                book = Books()
            book.book_title = self.cleaned_data['book_title']
            book.date_of_pub = self.cleaned_data['date_of_pub']
            book.isbn_number = self.cleaned_data['isbn_number']
            book.book_author = self.cleaned_data['book_author']
            book.book_category = self.cleaned_data['book_category']
            book.qty_in_lib = self.cleaned_data['qty_in_lib']
            book.save()
            return book

        class Meta:
                model = Books

class UserForm(ModelForm):
        ud_id = forms.IntegerField(widget=forms.HiddenInput(),required=False)

        def save(self, force_insert=False, force_update=False, commit=True):
            u = super(UserForm, self).save(commit=False)
            try:
                users = User.objects.get(id = self.cleaned_data['ud_id'])
            except:
                users = User
            users.username = self.celaned_data['username']
            return users

