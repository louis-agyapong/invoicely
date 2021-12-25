from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Client(models.Model):
    name = models.CharField(_("name"), max_length=255)
    email = models.EmailField(_("email"))
    org_number = models.CharField(_("organisation's number"), max_length=255)
    address_1 = models.CharField(_("address"), max_length=255, blank=True)
    address_2 = models.CharField(_("address"), max_length=255, blank=True)
    zip_code = models.CharField(_("zip code"), max_length=255, blank=True)
    place = models.CharField(_("place"), max_length=255, blank=True)
    country = models.CharField(_("country"), max_length=255, blank=True)
    contact_person = models.CharField(_("contact person"), max_length=255, blank=True)
    contact_reference = models.CharField(_("contact reference"), max_length=255, blank=True)
    created_by = models.ForeignKey(User, related_name="clients", on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    def __str__(self):
        return self.name
