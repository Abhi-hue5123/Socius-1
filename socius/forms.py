from django import forms
from socius.models import DirectoryCreation

class DirectoryCreationForm(forms.ModelForm):
    class Meta:
        model=DirectoryCreation
        fields=('DirectoryName','Description','img','MembersLimit',)
        