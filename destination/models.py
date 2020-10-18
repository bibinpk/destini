from django.db import models


# Create your models here.

class destination(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Name")
    district = models.ForeignKey('districts', on_delete=models.CASCADE)
    place = models.CharField(max_length=50, verbose_name="Place")
    route_road = models.CharField(max_length=100, verbose_name="By road")
    route_air = models.CharField(max_length=100, verbose_name="By air")
    route_rail = models.CharField(max_length=100, verbose_name="By rail")
    best_time = models.TextField(verbose_name="Best time for visit")
    Things_to_do = models.TextField(verbose_name="Things to do")
    type = models.CharField(max_length=200, verbose_name="Type")
    image = models.ImageField(upload_to='pics', verbose_name="Picture")

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Destination'
        verbose_name_plural = 'Destinations'


class districts(models.Model):
    name = models.CharField(max_length=25)


    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'District'
        verbose_name_plural = 'Districts'


class popular(models.Model):
    name = models.ForeignKey('destination', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Popular'
        verbose_name_plural = 'Popular'