from django.contrib import admin

from models import Account
from user_auths.models import User
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class AccountAdminModel(ImportExportModelAdmin):
    model = Account
    search_fields = ["full_name"]
    list_editable = ["account_status", "account_balence"]
    list_display = ["user", "account_number", "account_status", "account_balance"]
    list_filter = ["account_status"]

class KYCAdmin(ImportExportModelAdmin):
    model = Account
    search_fields = ["full_name"]
    list_display = ["user", "full_name"]
    
