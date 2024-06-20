from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class VerificationCodeModel(models.Model):
    code = models.CharField(max_length=6, unique=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='verification_codes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Verification Code'
        verbose_name_plural = 'Verification Codes'


class TeamModel(models.Model):
    image = models.ImageField()
    full_name = models.CharField(max_length=128)
    job = models.CharField(max_length=128)
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class AccountModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='accounts')
    full_name = models.CharField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.full_name)

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')