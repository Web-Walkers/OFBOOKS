from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, email, password, **extra_fields)
    
    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not name: name = email
        return self._create_user(name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email           = models.EmailField(unique=True)
    name            = models.CharField(max_length=255, blank=True, default='')
    biography       = models.TextField(blank=True)
    avatar          = models.ImageField(upload_to='avatars', blank=True, null=True)

    is_active       = models.BooleanField(default=True)
    is_superuser    = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_premium      = models.BooleanField(default=False)

    date_joined     = models.DateTimeField(default=timezone.now)
    last_login      = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return str(self.name)
    

    def get_avatar(self):
        if self.avatar:
            return settings.WEBSITE_URL + self.avatar.url
        else:
            return ''
    
    class Meta:
        verbose_name = _('کاربر')
        verbose_name_plural = _('کاربران')


# --- Address ---
class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name='نام گیرنده')
    phone = PhoneNumberField(null=False, blank=False, verbose_name='شماره تماس گیرنده')
    province = models.CharField(max_length=128, verbose_name='استان')
    city = models.CharField(max_length=128, verbose_name='شهر')
    address = models.TextField(verbose_name='آدرس پستی')
    zip_code = models.CharField(max_length=128, verbose_name='کد پستی')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', blank=False, null=True)

    def get_full_address(self):
        return f"{self.province} - {self.city} - {self.address}"
    
    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"


# --- Faaliat ---
class Faaliat(models.Model):
    detail = models.TextField(verbose_name='جزئیات')
    link = models.CharField(max_length=255, verbose_name='نوع')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Faaliatha', blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.detail if len(self.detail) < 20 else self.detail[:18] + '...'
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('فعالیت')
        verbose_name_plural = _('فعالیت ها')
    

"""
                        ...----....
                    ..-:"''         ''"-..
                 .-'                      '-.
               .'              .     .       '.
             .'   .          .    .      .    .''.
           .'  .    .       .   .   .     .   . ..:.
         .' .   . .  .       .   .   ..  .   . ....::.
        ..   .   .      .  .    .     .  ..  . ....:IA.
       .:  .   .    .    .  .  .    .. .  .. .. ....:IA.
      .: .   .   ..   .    .     . . .. . ... ....:.:VHA.
      '..  .  .. .   .       .  . .. . .. . .....:.::IHHB.
     .:. .  . .  . .   .  .  . . . ...:.:... .......:HIHMM.
    .:.... .   . ."::"'.. .   .  . .:.:.:II;,. .. ..:IHIMMA
    ':.:..  ..::IHHHHHI::. . .  ...:.::::.,,,. . ....VIMMHM
   .:::I. .AHHHHHHHHHHAI::. .:...,:IIHHHHHHMMMHHL:. . VMMMM
  .:.:V.:IVHHHHHHHMHMHHH::..:" .:HIHHHHHHHHHHHHHMHHA. .VMMM.
  :..V.:IVHHHHHMMHHHHHHHB... . .:VPHHMHHHMMHHHHHHHHHAI.:VMMI
  ::V..:VIHHHHHHMMMHHHHHH. .   .I":IIMHHMMHHHHHHHHHHHAPI:WMM
  ::". .:.HHHHHHHHMMHHHHHI.  . .:..I:MHMMHHHHHHHHHMHV:':H:WM
  :: . :.::IIHHHHHHMMHHHHV  .ABA.:.:IMHMHMMMHMHHHHV:'. .IHWW
  '.  ..:..:.:IHHHHHMMHV" .AVMHMA.:.'VHMMMMHHHHHV:' .  :IHWV
   :.  .:...:".:.:TPP"   .AVMMHMMA.:. "VMMHHHP.:... .. :IVAI
  .:.   '... .:"'   .   ..HMMMHMMMA::. ."VHHI:::....  .:IHW'
  ...  .  . ..:IIPPIH: ..HMMMI.MMMV:I:.  .:ILLH:.. ...:I:IM
: .   .'"' .:.V". .. .  :HMMM:IMMMI::I. ..:HHIIPPHI::'.P:HM.
:.  .  .  .. ..:.. .    :AMMM IMMMM..:...:IV":T::I::.".:IHIMA
'V:.. .. . .. .  .  .   'VMMV..VMMV :....:V:.:..:....::IHHHMH
  "IHH:.II:.. .:. .  . . . " :HB"" . . ..PI:.::.:::..:IHHMMV"
   :IP""HHII:.  .  .    . . .'V:. . . ..:IH:.:.::IHIHHMMMMM"
   :V:. VIMA:I..  .     .  . .. . .  .:.I:I:..:IHHHHMMHHMMM
   :"VI:.VWMA::. .:      .   .. .:. ..:.I::.:IVHHHMMMHMMMMI
   :."VIIHHMMA:.  .   .   .:  .:.. . .:.II:I:AMMMMMMHMMMMMI
   :..VIHIHMMMI...::.,:.,:!"I:!"I!"I!"V:AI:VAMMMMMMHMMMMMM'
   ':.:HIHIMHHA:"!!"I.:AXXXVVXXXXXXXA:."HPHIMMMMHHMHMMMMMV
     V:H:I:MA:W'I :AXXXIXII:IIIISSSSSSXXA.I.VMMMHMHMMMMMM
       'I::IVA ASSSSXSSSSBBSBMBSSSSSSBBMMMBS.VVMMHIMM'"'
        I:: VPAIMSSSSSSSSSBSSSMMBSSSBBMMMMXXI:MMHIMMI
       .I::. "H:XIIXBBMMMMMMMMMMMMMMMMMBXIXXMMPHIIMM'
       :::I.  ':XSSXXIIIIXSSBMBSSXXXIIIXXSMMAMI:.IMM
       :::I:.  .VSSSSSISISISSSBII:ISSSSBMMB:MI:..:MM
       ::.I:.  ':"SSSSSSSISISSXIIXSSSSBMMB:AHI:..MMM.
       ::.I:. . ..:"BBSSSSSSSSSSSSBBBMMMB:AHHI::.HMMI
       :..::.  . ..::":BBBBBSSBBBMMMB:MMMMHHII::IHHMI
       ':.I:... ....:IHHHHHMMMMMMMMMMMMMMMHHIIIIHMMV"
         "V:. ..:...:.IHHHMMMMMMMMMMMMMMMMHHHMHHMHP'
          ':. .:::.:.::III::IHHHHMMMMMHMHMMHHHHM"
            "::....::.:::..:..::IIIIIHHHHMMMHHMV"
              "::.::.. .. .  ...:::IIHHMMMMHMV"
                "V::... . .I::IHHMMV"'
                  '"VHVHHHAHHHHMMV:"'
"""