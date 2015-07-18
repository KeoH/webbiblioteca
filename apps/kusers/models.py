from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save

class Person(models.Model):

    user            = models.OneToOneField(
                        User,
                        verbose_name=_("User")
                    )
    photo           = models.ImageField(
                        upload_to="users/photo",
                        blank=True
                    )

    class Meta:
        abstract    = True

    def __unicode__(self):
        return self.user.username


class Kuser(Person):

    cargo           = models.CharField(
                        blank=True,
                        max_length=255,
                        default='-'
                    )
    departamento    = models.CharField(
                        blank=True,
                        max_length=255,
                        default='-'
                    )
    customer        = models.BooleanField(
                        default=True
                    )

    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')

# Creamos la conexion entre usuario y KUsers

def create_kuser(sender, instance, **kwargs):
    p = Kuser.objects.get_or_create(user=instance)

post_save.connect(create_kuser, sender=User, dispatch_uid='KUser creado')
