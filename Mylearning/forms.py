from django import forms
from django.core import validators
from Mylearning.models import Reg_Form
# define below forms classes ...


class StudentReg(forms.Form):
        Fname = forms.CharField()
        Lname = forms.CharField()
        Email = forms.EmailField()
        text = forms.CharField(widget=forms.Textarea)
        botcapt = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])



class StudentRegForm(forms.ModelForm):

    class Meta:
        model = Reg_Form
        fields = '__all__'


