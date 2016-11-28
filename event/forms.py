from django import forms


class Participant(forms.Form):
    name=forms.CharField(label="name",max_length=100)
    value=forms.CharField(label="value")
