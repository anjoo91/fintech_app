from django.contrib import admin

from requests import request
from models import Account
from user_auths.models import User
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
from sorl.thumbnail import get_thumbnail
from django.utils.safestring import mark_safe
from django import forms

# Register your models here.
class AccountAdminModel(ImportExportModelAdmin):
    model = Account
    search_fields = ["full_name"]
    list_editable = ["account_status", "account_balence"]
    list_display = ["user", "account_number", "account_status", "account_balance"]
    list_filter = ["account_status"]
    