from django import forms

class Tweet(forms.Form):
    author = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Author"}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Comment"}))
    # image = forms.ImageField()