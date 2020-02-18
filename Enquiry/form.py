from django.contrib.auth.models import User
from django import forms
from Enquiry.models import Enquiry


class UserEnquiryForm(forms.ModelForm):

    class Meta:
        model = Enquiry
        fields = ('company_enquire_name',
                  'email',
                  'phone',
                  'address_location',
                  'service_product',
                  'requirements',
                  'file')
        widgets = {
            'company_enquire_name': forms.TextInput(attrs={'placeholder': ' Enter Name/ Company', 'size': 'auto'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
            'address_location': forms.TextInput(attrs={'placeholder': 'Location/ City'}),
            'service_product': forms.TextInput(attrs={'placeholder': 'Product/ Service'}),
            'requirements': forms.Textarea(attrs={'placeholder': 'Describe here'}),

        }


