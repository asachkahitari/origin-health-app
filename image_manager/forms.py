from django import forms
from .models import Image

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'label']

class ImageDeleteForm(forms.Form):
    image_id = forms.IntegerField(widget=forms.HiddenInput())

class ImageEditForm(forms.Form):
    image_id = forms.IntegerField(widget=forms.HiddenInput())
    new_label = forms.CharField(max_length=255)
