from django import forms


class UploadImageForm(forms.Form):
    username = forms.CharField(max_length=128)
    file = forms.FileField()
