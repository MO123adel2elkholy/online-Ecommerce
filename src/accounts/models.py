from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _
import datetime
from django.utils.text import slugify
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField( User, verbose_name=_('user'),on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    country = models.CharField(max_length=50)
    prfile_image = models.ImageField(upload_to='profile_images', verbose_name=_('profile image'), null=True, blank=True)
    address = models.CharField(max_length=100)
    joinDate =models.DateTimeField(_('joinDate'), default=datetime.datetime.now())


    def __str__(self):
        return str(self.user)


    def get_absolute_url(self):

        return reverse('profile_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)



def create_profile(sender, **kwargs) :
    if kwargs['created']:
        user_prrofile= Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)