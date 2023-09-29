from django import forms
from .models import Account
from shortuuid import ShortUUID

class AccountAdminForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(AccountAdminForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Only set if creating a new object
            self.initial['account_number'] = ShortUUID().random(length=10)
            self.initial['account_id'] = ShortUUID().random(length=7)
            self.initial['ref_code'] = ShortUUID().random(length=10)
