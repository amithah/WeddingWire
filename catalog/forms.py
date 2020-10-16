from page.models import Page
from django import  forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

DESIGN_CHOICES = [
        ('DESIGN_1', 'Design 1'),
        ('DESIGN_2', 'Design 2'),
        ('DESIGN_3', 'Design 2'),
        ('DESIGN_4', 'Design 4'),
    ]


class CreateWebsiteForm(forms.Form):
    groom_name = forms.CharField(max_length=200, )
    bride_name = forms.CharField(max_length=200, )
    email = forms.EmailField(required=True)
    design = forms.ChoiceField(choices=DESIGN_CHOICES)
    city = forms.CharField(max_length=200, )
    date = forms.DateField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('create', 'Create Website'))


# class PageCreationForm(ModelForm):
#     class Meta:
#         model = Page
#         fields = ['groom_name','bride_name','email','design','city','date']



