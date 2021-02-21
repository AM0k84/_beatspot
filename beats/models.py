from django.db import models
from embed_video.fields import EmbedVideoField
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from django.conf import settings

from users.models import Profile


class Base(models.Model):
    created_on = models.DateTimeField(_("created"), auto_now_add=True, null=True)
    edit_date = models.DateTimeField(_("edited"), auto_now=True)


class BeatCategory(Base):
    category_name = models.CharField(_('category name'), max_length=128)
    slug = models.SlugField(null=False, unique=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Beat category")
        verbose_name_plural = _("Beat categories")
        ordering = ("id",)

    def __str__(self):
        return self.category_name


class Beat(Base):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='beat_author')

    beat_title = models.CharField(_("beat title"), max_length=120)
    beat_link = EmbedVideoField(_("beat link"), blank=False, null=False)
    beat_category = models.ForeignKey(BeatCategory, on_delete=models.CASCADE, related_name='categories',
                                      verbose_name=_("beat category"))
    slug = models.SlugField(null=False, unique=False)
    is_promoted = models.BooleanField(default=False)
    price = models.SmallIntegerField(null=True, blank=True)
    likes = models.ManyToManyField(Profile, default=None, blank=True, related_name='likes')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.beat_title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Beat")
        verbose_name_plural = _("Beats")
        ordering = ("id",)

    def __str__(self):
        return self.beat_title


