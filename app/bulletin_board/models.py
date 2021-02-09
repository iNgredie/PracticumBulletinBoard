import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """Custom user model"""

    ROLES = [
        ("user", "user"),
        ("moderator", "moderator"),
        ("admin", "admin"),
    ]
    STATUS_LIST = [
        ("blocked", "blocked"),
        ("active", "active"),
        ("email verification", "email verification"),
    ]
    username = None
    first_name = models.CharField("name", max_length=255)
    last_name = models.CharField("last name", max_length=255)
    role = models.CharField("role", max_length=9, choices=ROLES, default="user")
    email = models.EmailField("email", unique=True)
    phone_number = PhoneNumberField(unique=True)
    time_to_call = models.CharField("time to call", max_length=3000)
    status = models.CharField(
        "status", max_length=20, choices=STATUS_LIST, default="active"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Ad(models.Model):
    """Ad model"""

    STATUS_LIST = [
        ("draft", "draft"),
        ("moderation", "moderation"),
        ("rejected", "rejected"),
        ("sales", "sales"),
        ("active", "active"),
    ]

    title = models.CharField("title", max_length=500)
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, verbose_name="category"
    )
    city = models.ForeignKey(
        "CitiesDirectory", on_delete=models.CASCADE, verbose_name="city"
    )
    description = models.TextField("description")
    publication_date = models.DateTimeField("publication date", auto_now_add=True)
    price = models.DecimalField("price", max_digits=9, decimal_places=2)
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="owner"
    )
    views = models.IntegerField("views", default=0, editable=False)
    photos = models.ImageField("photos", upload_to="photos/")
    status = models.CharField("status", max_length=20, choices=STATUS_LIST)
    created_at = models.DateTimeField("created at", auto_now_add=True)
    updated_at = models.DateTimeField("updated at", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Category(models.Model):
    """Category model"""

    title = models.CharField("title", max_length=255)
    uuid = models.UUIDField("uuid", default=uuid.uuid4, editable=False, unique=True)
    description = models.CharField("description", max_length=5000)
    created_at = models.DateTimeField("created at", auto_now_add=True)
    updated_at = models.DateTimeField("updated at", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class CitiesDirectory(models.Model):
    """CitiesDirectory model"""

    title = models.CharField("title", max_length=255)
    region = models.ForeignKey(
        "RegionDirectory", on_delete=models.CASCADE, verbose_name="region"
    )
    created_at = models.DateTimeField("created at", auto_now_add=True)
    updated_at = models.DateTimeField("updated at", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class RegionDirectory(models.Model):
    """RegionDirectory model"""

    title = models.CharField("title", max_length=255)
    created_at = models.DateTimeField("created at", auto_now_add=True)
    updated_at = models.DateTimeField("updated at", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class AdModerationRecord(models.Model):
    """AdModerationRecord model"""

    moderation_date = models.DateTimeField("moderation date", auto_now=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="ad")
    moderator = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="moderator"
    )
    created_at = models.DateTimeField("created at", auto_now_add=True)
    updated_at = models.DateTimeField("updated at", auto_now=True)
