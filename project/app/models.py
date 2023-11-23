from django.db import models

from django_tenants.models import TenantMixin,DomainMixin

class Client(TenantMixin):
    username = models.CharField(max_length=100)
    db_name = models.CharField(max_length=100)
    def __str__(self):
        return self.username  # This is just a string representation for the model
class Domain(DomainMixin):
    pass