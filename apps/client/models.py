from django.db import models


class Client(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = "client"
