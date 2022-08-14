from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class Food(models.Model):
    FOOD_TYPE = [
        ("brakefast", "صبحانه"),
        ("dinner", "شام"),
        ("lunch", "ناهار"),
        ("drinks", "نوشیدنی"),
    ]
    name = models.CharField(_("نام"), max_length=50)
    descriptions = models.CharField(_("توضیحات"), max_length=50)
    price = models.IntegerField(_("قیمت"))
    time = models.TimeField(_("زمان"), auto_now=False, auto_now_add=False)
    pubdate = models.DateField(
        _("تاریخ انتشار"), auto_now=False, auto_now_add=False)
    photo = models.ImageField(_("عکس"), upload_to='foods/')
    type_food = models.CharField(
        _("نوع غذا"), max_length=50, choices=FOOD_TYPE, default="شام")

    def __str__(self):
        return(self.name)
