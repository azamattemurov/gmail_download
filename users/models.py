from django.db import models


class UserConfirmationModel(models.Model):
    objects = None
    code = models.IntegerField()
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'code'
        verbose_name_plural = 'codes'
