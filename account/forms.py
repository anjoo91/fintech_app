from django import forms
from .models import Account, KYC
from django.forms import ImageField, FileInput, DateInput
from shortuuid import ShortUUID

class AccountAdminForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(AccountAdminForm, self).__init__(*args, **kwargs)
        # if these fields are empty, generate a ShortUUID of specific lengths for each field (new account)
        # otherwise, use the value already in the field (existing account)
        if not self.instance.account_number:
            self.initial['account_number'] = ShortUUID().random(length=10)
        if not self.instance.account_id:
            self.initial['account_id'] = ShortUUID().random(length=7)
        if not self.instance.ref_code:
            self.initial['ref_code'] = ShortUUID().random(length=10)


class DateInput(forms.DateInput):
    input_type = 'date'
    
class KYCForm(forms.ModelForm):
    identity_image = ImageField(widget=FileInput)
    image = ImageField(widget=FileInput)
    
    class Meta:
        model = KYC
        fields = [
            'full_name',
            'image',
            'marital_status',
            'gender',
            'identity_type',
            'identity_image',
            'date_of_birth',
            'signature',
            'country',
            'state',
            'city',
            'mobile',
            'fax',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name',}),
            "mobile": forms.TextInput(attrs={'placeholder': 'Mobile',}),
            "fax": forms.TextInput(attrs={'placeholder': 'Fax',}),
            "country": forms.TextInput(attrs={'placeholder': 'Country',}),
            "state": forms.TextInput(attrs={'placeholder': 'State',}),
            "city": forms.TextInput(attrs={'placeholder': 'City',}),
        }