from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContentEditForm(forms.Form):
    groom_name = forms.CharField(max_length=200, )
    bride_name = forms.CharField(max_length=200, )
    city = forms.CharField(max_length=200, )
    date = forms.DateField()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.add_input(Submit('save', 'Save'))


class ImageAddForm(forms.Form):
    bride_image= forms.ImageField()
    groom_image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('save', 'Save'))
