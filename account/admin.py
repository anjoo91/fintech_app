from django.contrib import admin
from .models import Account, KYC
from user_auths.models import User
from import_export.admin import ImportExportModelAdmin
from .forms import AccountAdminForm


# Register your models here.
class AccountAdminModel(ImportExportModelAdmin):
    form = AccountAdminForm # use custom form
    list_editable = ["account_status", "account_balance"]
    list_display = ["user", "account_number", "account_status", "account_balance"]
    list_filter = ["account_status"]

class KYCAdmin(ImportExportModelAdmin):
    search_fields = ["full_name"]
    list_display = ["user", "full_name"]
    
admin.site.register(Account, AccountAdminModel)
admin.site.register(KYC, KYCAdmin)