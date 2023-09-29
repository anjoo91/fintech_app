from django import forms
from .models import Account
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

