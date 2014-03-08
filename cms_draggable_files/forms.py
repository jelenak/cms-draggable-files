from django import forms

class FileForm(forms.Form):
    dragged_files = forms.FileField(label='Select a file')