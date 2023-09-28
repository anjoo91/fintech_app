from django.db import models
import uuid
from shortuuidfield import ShortUUIDField
from  user_auths.models import User

ACCOUNT_STATUS = (
    ("active", "Active"),
    ("inactive", "Inactive"),
)

MARITAL_STATUS = (
    ("married", "Married"),
    ("single", "Single"),
    ("other", "Other"),
)

def user_directory_path(instance, filename):
    #Grab the file extension
    ext = filename.split('.')[-1]
    filename="%s_%s_%s" % (instance.id, ext)
    #return the whole path to the file
    return "user_{0}/{1}".format(instance.user.id, filename)


class Account(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    account_number = ShortUUIDField(length=10, max_length=25, prefix="217", alphabet="0123456789", unique=True)
    account_id = ShortUUIDField(length=7, max_length=25, prefix="BKM", alphabet="0123456789", unique=True)
    pin_number = ShortUUIDField(length=4, max_length=7, alphabet="0123456789", unique=True)
    ref_code = ShortUUIDField(length=10, max_length=25, alphabet="abcdefghijklmnopqrstuvwxyz0123456789", unique=True)