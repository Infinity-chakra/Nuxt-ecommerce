from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.model(email=email)
        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Email", unique=True, max_length=255)
    username = models.CharField("User Name", unique=True, max_length=255, blank=True, null=True)
    firstName = models.CharField("First Name", max_length=100, blank=True, null=True)
    lastName = models.CharField("Last Name", max_length=100, blank=True, null=True)
    is_active = models.BooleanField('Active', default=True)
    is_staff = models.BooleanField('Staff', default=False)
    is_superuser = models.BooleanField('Super User', default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "User"


class Item(models.Model):
    product_id = models.CharField("Product Id", max_length=100, blank=True, null=True)
    title = models.CharField("Title", max_length=300, blank=True, null=True)
    link = models.CharField("Link", max_length=200, blank=True, null=True)
    price = models.IntegerField("Price", blank=True, null=True)
    mrp = models.IntegerField("MRP", blank=True, null=True)
    brand = models.CharField("Brand", max_length=200, blank=True, null=True)
    rating = models.FloatField("Rating", blank=True, null=True)
    totalRating = models.IntegerField("Total Rating", blank=True, null=True)
    discount = models.IntegerField("Discount", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "Items"
