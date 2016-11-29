from django import forms


class Participant(forms.Form):
    name=forms.CharField(label="name",max_length=100,required=True)
    value=forms.CharField(label="value")
    email=forms.EmailField(required=True,label="email")
