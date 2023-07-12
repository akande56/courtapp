from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for courtapp.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_judge = models.BooleanField(null=True)
    is_chief_judge = models.BooleanField(null=True)
    is_lawyer = models.BooleanField(null=True)
    is_clerk = models.BooleanField(null=True)
    is_defendant = models.BooleanField(null=True)
    is_plaintief = models.BooleanField(null=True)
    

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
    
    def save(self, *args, **kwargs):
        if self.is_judge:
            self.is_chief_judge = False
            self.is_lawyer = False
            self.is_defendant = False
            self.is_plaintief = False
        elif self.is_chief_judge:
            self.is_judge = False
            self.is_lawyer = False
            self.is_defendant = False
            self.is_plaintief = False
        elif self.is_lawyer:
            self.is_judge = False
            self.is_chief_judge = False
            self.is_defendant = False
            self.is_plaintief = False
        elif self.is_defendant:
            self.is_judge = False
            self.is_chief_judge = False
            self.is_lawyer = False
            self.is_plaintief = False
        elif self.is_plaintief:
            self.is_judge = False
            self.is_chief_judge = False
            self.is_lawyer = False
            self.is_defendant = False

        return super().save(*args, **kwargs)

