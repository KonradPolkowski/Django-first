from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default="")
    premiere = models.DateField(null=True, blank=True)
    imbd_rating = models.DecimalField(max_digits=4, decimal_places=2,
                                      null=True)
    picture = models.ImageField(upload_to="Pictures", null=True, blank=True)

    # def __str__(self):
    #    return self.title + " (" + str(self.year) + ")"

    def __str__(self):
        return self.titleWithYear()

    def titleWithYear(self):
        return "{} ({})".format(self.title, self.year)
