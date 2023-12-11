"""Custom user model and manager are defined here."""
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import Group, Permission

# Create your models here.
class UserManager(BaseUserManager):
    """Custom manager for creating and validating users"""

    def create_user(self, email, username, password=None):
        """Give username and password to create a new user"""
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have a username")
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username):
        """Create a new superuser"""
        user = self.create_user(
            email=self.normalize_email(email), username=username, password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


def get_profile_imagepath(self):
    """Saving the profile image at a specific path."""
    return f'profile_images/{self.pk}/{"profile_image.png"}'


def get_default_profile_imagepath():
    """getting default image if no image is specified."""
    return "image/profile_default.jpg"


class OlxUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model inheriting from AbstractBaseUser with email as login field."""

    class ApproveChoices(models.IntegerChoices):
        Stasis = 0
        Approved = 1
        Rejected = 2

    email = models.CharField(verbose_name="email", max_length=250, unique=True)
    username = models.CharField(verbose_name="username", max_length=255, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_approved = models.IntegerField(choices=ApproveChoices.choices, default=ApproveChoices.Stasis)
    groups = models.ManyToManyField(Group, related_name='olx_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='olx_user_permissions')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return str(self.username)

    def get_profile_image_filename(self):
        """for getting profile image filename"""
        return str(self.profile_image)[
            str(self.profile_image).index(f"profile_images/{self.pk}/") :
        ]

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class OlxUserProfile(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = PhoneNumberField(blank=True)
    address = models.TextField()
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    user = models.OneToOneField(OlxUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
