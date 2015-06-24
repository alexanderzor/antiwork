# -*- coding: utf-8
from django import forms
from django.forms import TextInput
from models import Feedback, Comment
from models import Company



class FeedBackForm(forms.Form):
    first_name = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Имя'}), required=False)
    email = forms.EmailField(widget=TextInput(attrs={'placeholder': u'E-mail'}), required=False)
    phone = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Телефон'}), required=False)
    text = forms.CharField(widget=forms.Textarea, required=True)
    file = forms.FileField(required=False)
    company = forms.CharField()

    def save(self, commit=True):
        feedback = Feedback.objects.create(first_name=self.cleaned_data['first_name'],
                                           email=self.cleaned_data['email'],
                                           phone=self.cleaned_data['phone'],
                                           message=self.cleaned_data['text'],
                                           company=Company.objects.filter(title=self.cleaned_data['company']).first(),
                                           )
        if not feedback.first_name:
            feedback.first_name = 'Анонимный пользователь'
        if commit:
            feedback.save()
        return feedback


class CommentForm(forms.Form):
    name = forms.CharField(max_length=20)
    content = forms.CharField(widget=forms.Textarea)

class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Поиск'}), required=True)