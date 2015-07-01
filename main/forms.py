# -*- coding: utf-8
from django import forms
from django.forms import TextInput
from models import Feedback, FeedbackComment, NewsComment
from models import Company
from ckeditor.widgets import CKEditorWidget


class FeedBackForm(forms.Form):
    first_name = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Имя'}), required=False)
    email = forms.EmailField(widget=TextInput(attrs={'placeholder': u'E-mail'}), required=False)
    phone = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Телефон'}), required=False)
    text = forms.CharField(widget=CKEditorWidget())
    file = forms.FileField(required=False)
    image = forms.ImageField(required=False)
    company = forms.CharField(required=False)
    url = forms.URLField(required=False)
    city = forms.CharField(max_length=25, required=False)

    def save(self, commit=True):
        files = self.files
        s = self.cleaned_data['first_name'] + self.cleaned_data['text'] + self.cleaned_data['company'] + self.cleaned_data['url'] + self.cleaned_data['city']
        feedback = Feedback.objects.create(first_name=self.cleaned_data['first_name'],
                                           email=self.cleaned_data['email'],
                                           phone=self.cleaned_data['phone'],
                                           description=self.cleaned_data['text'],
                                           company=self.cleaned_data['company'],
                                           url=self.cleaned_data['url'],
                                           city=self.cleaned_data['city'],
                                           keywords=s
                                           )
        if files:
            feedback.image = self.files['image']
        if not feedback.first_name:
            feedback.first_name = 'Анонимный пользователь'
            feedback.anon = True
        if commit:
            feedback.save()
        return feedback


class CommentForm(forms.Form):
    name = forms.CharField(max_length=20)
    content = forms.CharField(widget=forms.Textarea)

class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Поиск'}), required=True)