from django.db import models
import uuid
from shortuuid import ShortUUID
from shortuuidfield import ShortUUIDField
from user_auths.models import User
from django.db.models.signals import post_save

ACCOUNT_STATUS = (
    ("active", "Active"),
    ("inactive", "Inactive"),
)

MARITAL_STATUS = (
    ("married", "Married"),
    ("single", "Single"),
    ("other", "Other"),
)

GENDER = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
)

NATIONALITY = (
    ("united_states_of_america", "United States of America"),
    ("united_kingdom", "United Kingdom"),
    ("france", "France"),
    ("canada", "Canada"),
    ("germany", "Germany"),
    ("australia", "Australia"),
    ("mexico", "Mexico"),
    ("spain", "Spain"),
    ("italy", "Italy"),
    ("netherlands", "Netherlands"),
    ("south_africa", "South Africa"),
    ("switzerland", "Switzerland"),
    ("japan", "Japan"),
    ("china", "China"),
    ("india", "India"),
    ("brazil", "Brazil"),
    ("russia", "Russia"),
    ("south_korea", "South Korea"),
    ("poland", "Poland"),
    ("philippines", "Philippines"),
    ("indonesia", "Indonesia"),
    ("turkey", "Turkey"),
    ("saudi_arabia", "Saudi Arabia"),
    ("argentina", "Argentina"),
    ("sweden", "Sweden"),
    ("norway", "Norway"),
    ("austria", "Austria"),
    ("belgium", "Belgium"),
    ("denmark", "Denmark"),
    ("finland", "Finland"),
    ("ireland", "Ireland"),
    ("new_zealand", "New Zealand"),
    ("singapore", "Singapore"),
    ("hong_kong", "Hong Kong"),
    ("malaysia", "Malaysia"),
    ("thailand", "Thailand"),
    ("vietnam", "Vietnam"),
    ("egypt", "Egypt"),
    ("nigeria", "Nigeria"),
    ("kenya", "Kenya"),
    ("ghana", "Ghana"),
    ("tanzania", "Tanzania"),
    ("uganda", "Uganda"),
    ("zimbabwe", "Zimbabwe"),
    ("zambia", "Zambia"),
    ("botswana", "Botswana"),
    ("namibia", "Namibia"),
    ("mozambique", "Mozambique"),
    ("angola", "Angola"),
    ("ethiopia", "Ethiopia"),
    ("morocco", "Morocco"),
    ("algeria", "Algeria"),
    ("tunisia", "Tunisia"),
    ("libya", "Libya"),
    ("cameroon", "Cameroon"),
    ("ivory_coast", "Ivory Coast"),
    ("senegal", "Senegal"),
    ("madagascar", "Madagascar"),
    ("mauritius", "Mauritius"),
    ("reunion", "Reunion"),
    ("mauritania", "Mauritania"),
    ("benin", "Benin"),
    ("burkina_faso", "Burkina Faso"),
    ("burundi", "Burundi"),
    ("chad", "Chad"),
    ("congo", "Congo"),
    ("djibouti", "Djibouti"),
    ("eritrea", "Eritrea"),
    ("gabon", "Gabon"),
    ("gambia", "Gambia"),
    ("guinea", "Guinea"),
    ("guinea_bissau", "Guinea-Bissau"),
    ("lesotho", "Lesotho"),
    ("liberia", "Liberia"),
    ("malawi", "Malawi"),
    ("mali", "Mali"),
    ("mauritania", "Mauritania"),
    ("niger", "Niger"),
    ("rwanda", "Rwanda"),
    ("sierra_leone", "Sierra Leone"),
    ("somalia", "Somalia"),
    ("sudan", "Sudan"),
    ("togo", "Togo"),
    ("tunisia", "Tunisia"),
    ("western_sahara", "Western Sahara"),
    ("central_african_republic", "Central African Republic"),
    ("equatorial_guinea", "Equatorial Guinea"),
    ("sao_tome_and_principe", "Sao Tome and Principe"),
    ("seychelles", "Seychelles"),
    ("swaziland", "Swaziland"),
    ("comoros", "Comoros"),
    ("cape_verde", "Cape Verde"),
    ("mayotte", "Mayotte"),
    ("guyana", "Guyana"),
    ("suriname", "Suriname"),
    ("french_guiana", "French Guiana"),
    ("martinique", "Martinique"),
    ("guadeloupe", "Guadeloupe"),
    ("haiti", "Haiti"),
    ("bahamas", "Bahamas"),
    ("barbados", "Barbados"),
    ("belize", "Belize"),
    ("costa_rica", "Costa Rica"),
    ("cuba", "Cuba"),
    ("dominica", "Dominica"),
    ("dominican_republic", "Dominican Republic"),
    ("el_salvador", "El Salvador"),
    ("grenada", "Grenada"),
    ("guatemala", "Guatemala"),
    ("other", "Other"),
)

IDENTITY_TYPE = (
    ("passport", "Passport"),
    ("drivers_license", "Driver's License"),
    ("national_id", "National ID"),
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
    account_number = models.CharField(max_length=25, unique=True, blank=True, null=True)
    account_id = models.CharField(max_length=25, unique=True, blank=True, null=True)
    pin_number = models.CharField(max_length=4, blank=False, null=False, default="0000")
    ref_code = models.CharField(max_length=25, unique=True, blank=True, null=True)
    account_status = models.CharField(max_length=100, choices=ACCOUNT_STATUS, default="inactive")
    date = models.DateTimeField(auto_now_add=True)
    kyc_submitted = models.BooleanField(default=False)
    kyc_confirmed = models.BooleanField(default=False)
    recommended_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="referral", null=True, blank=True)
    
    class Meta: 
        # desc date
        ordering = ['-date']
    
    def __str__(self):
        try: 
            return self.user
        except:
            return "Account Model"

    # Overwritting the save method to generate a ShortUUID of specific lengths for each field
    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = ShortUUID().random(length=10)
        if not self.account_id:
            self.account_id = ShortUUID().random(length=7)
        if not self.ref_code:
            self.ref_code = ShortUUID().random(length=10)
    
        super(Account, self).save(*args, **kwargs)
        
#Automatically reate an account for every new user        
def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

#Save the account when the user is saved
def save_account(sender, instance, **kwargs):
    instance.account.save()

#Connect the signals    
post_save.connect(create_account, sender=User)
post_save.connect(save_account, sender=User)