from django import forms

class SentimentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Enter Your text here...", "rows":4, "cols":40}),
                           label = "Text")