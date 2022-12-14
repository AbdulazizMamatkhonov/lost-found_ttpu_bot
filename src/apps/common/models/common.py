from django.db import models


class LanguageChoice(models.TextChoices):
    ENGLISH = "๐บ๐ธ English", "en"
    RUSSIAN = "๐ท๐บ ะ ัััะบะธะน", "ru"
    UZBEK = "๐บ๐ฟ O'zbekcha", "uz"


class StatusChoices(models.IntegerChoices):
    CREATED = 1, "Created"
    PUBLISHED = 2, "Published"
    DELIVERED = 3, "Delivered"
    CANCELLED = 4, "Cancelled"
    REJECTED = 5, "Rejected"
    BLOCKED = 6, "Blocked"


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
