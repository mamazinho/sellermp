from django.db import models

# Create your models here.


class Seller(models.Model):

    id = models.AutoField(
        primary_key=True
    )
    cnpj = models.CharField(
        max_length=18,
        default='',
        unique=True
    )
    company_name = models.CharField(
        max_length=100,
        default=''
    )
    is_active = models.BooleanField(
        default=True
    )
    bank_name = models.CharField(
        max_length=100,
        default=''
    )
    bank_account = models.IntegerField(
        default=0
    )
    bank_agency = models.IntegerField(
        default=0
    )

    def __str__(self):
        return f'{self.id} - {self.cnpj} - {self.company_name} - {self.bank_name} - {self.bank_account} - {self.bank_agency}'

    class Meta:
        managed = True
        db_table = 'Seller'


class SellerContact(models.Model):

    id = models.AutoField(
        primary_key=True
    )
    seller = models.ForeignKey(
        Seller,
        models.CASCADE,
        related_name='contacts'
    )
    address = models.CharField(
        max_length=100,
        default=''
    )
    responsible_email = models.EmailField(
        max_length=200,
        default=''
    )
    phone_number = models.BigIntegerField(
        default=0
    )

    def __str__(self):
        return f'{self.id} - {self.seller} - {self.address} - {self.responsible_email} - {self.phone_number}'

    class Meta:
        managed = True
        db_table = 'SellerContact'
