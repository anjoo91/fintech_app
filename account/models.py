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
    account_number = ShortUUIDField(length=10, max_length=25, prefix="217", alphabet="0123456789", unique=True)
    account_id = ShortUUIDField(length=7, max_length=25, prefix="BKM", alphabet="0123456789", unique=True)
    pin_number = ShortUUIDField(length=4, max_length=7, alphabet="0123456789", unique=True)
    ref_code = ShortUUIDField(length=10, max_length=25, alphabet="abcdefghijklmnopqrstuvwxyz0123456789", unique=True)
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
