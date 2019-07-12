from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

corpus_fund = 100000
membership_fund = 1500
legal_charges = 10000
consumer_fund = 30000


class UserManager(BaseUserManager):
    def create_user(self, username, status, password=None):
        if not username:
            raise ValueError('Users must have a username ')
        if not password:
            raise ValueError('Users must have a password ')

        user_obj = self.model(username=username, status=status)
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, username, status, password):
        user = self.create_user(username=username, password=password, status=status)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    flat_no = models.CharField(max_length=5, default=None, unique=True, null=True, blank=True)
    phone1 = models.IntegerField(null=True, blank=True, unique=True, default=None)
    phone2 = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    status_choice = [('O', 'Owner'), ('T', 'Tenant'), ('V', 'Vacant')]
    status = models.CharField(choices=status_choice, max_length=1, default=None)
    corpus_due = models.IntegerField(null=True, blank=True, unique=False, default=None)
    corpus_due_date = models.DateField(default=None, blank=True, null=True,)
    membership_due = models.IntegerField(null=True, blank=True, unique=False, default=None)
    membership_due_date = models.DateField(default=None, blank=True, null=True,)
    legal_charges_due = models.IntegerField(null=True, blank=True, unique=False, default=None)
    legal_charges_due_date = models.DateField(default=None, blank=True, null=True,)
    consumer_due = models.IntegerField(null=True, blank=True, unique=False, default=None)
    consumer_due_date = models.DateField(default=None, blank=True, null=True,)
    maintenance_due = models.IntegerField(null=True, blank=True, unique=False, default=None)
    maintenance_due_date = models.DateField(default=None, blank=True, null=True,)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['status']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self):
        return self.full_name

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff




