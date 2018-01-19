from django import forms
from django.forms import Form


class ContactForm(Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using self.cleaned_data dictionary
        pass


class BlogForm(Form):
    name = forms.CharField()
    tagline = forms.CharField()

class BlogEntryForm(Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea())
    pub_date = forms.DateTimeField()


    
    
    
    
    
    
    
    