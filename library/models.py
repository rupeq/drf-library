from django.db import models
from django.utils.translation import gettext as _

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE


class Authors(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name=_("Name"), max_length=50)

    class Meta:
        db_table = 'Author'
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def __str__(self):
        return self.name


class Books(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name=_("Title"), max_length=50)
    published_year = models.DateField(verbose_name=_("Published Year"))
    genre = models.CharField(verbose_name=_("Genre"), max_length=50)
    rating = models.DecimalField(verbose_name=_("Rating"), decimal_places=1, max_digits=2, null=True)
    author_id = models.ManyToManyField(Authors, verbose_name=_("Authors"), related_name=_("author_book"))

    class Meta:
        db_table = 'Book'
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return self.title
