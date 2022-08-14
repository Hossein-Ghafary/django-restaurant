from unicodedata import category
from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Blog (models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    description = models.CharField(_("توضیحات"), max_length=500)
    content = models.TextField(_("متن"))
    creates_at = models.DateTimeField(_("زمان انتشار"), default=timezone.now)
    auther = models.ForeignKey(User, verbose_name=_(
        "نویسنده"), on_delete=models.CASCADE)
    image = models.ImageField(_("تصویر"), upload_to="blog/",null = True)
    category = models.ForeignKey("Category",related_name="blog", verbose_name=_("دسته بندی"), on_delete=models.CASCADE , null=True)
    tags = models.ManyToManyField("Tag", verbose_name=_("تگ ها"),related_name="blogs",null=True)


    def __str__(self):
        return(self.title)

class Category(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    siug = models.SlugField(_("عنوان لاگین"))
    publish_at = models.DateTimeField(_(""), auto_now=False, auto_now_add=True)

    def __str__(self):
        return(self.title)

class Tag(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("نام لاتین"))
    publish_at = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(_("تاریخ آپدیت "), auto_now=True, auto_now_add=False)

    def __str__(self):
        return(self.title)