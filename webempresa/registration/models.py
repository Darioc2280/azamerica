from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

#con esto eliminamos el archivo existente reemplazando con el nuevo
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='usuario') #OneToOne solo puede tener un perfil para cada usuario, no puede dos perfiles para un mismo usuario ni disitnitios usuarios para un mismo perfil
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True, verbose_name='imagen avatar')
    bio = models.TextField(null=True, blank=True, verbose_name='Biografia')
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        #print("se acaba de crear un ususario y su perfil enlazado")