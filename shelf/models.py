from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _



class Author(models.Model):
    first_name = models.CharField( _("first name"),max_length = 20)
    last_name = models.CharField(max_length = 20)
    def __str__(self):
        return '{first_name}{last_name}'.format(first_name = self.first_name,last_name= self.last_name)

    class Meta:
        ordering = ('last_name', 'first_name')
        verbose_name = _('author')
        verbose_name_plural = _('authors')


class Publisher(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class BookCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    """cos w w rodzaju rekopisu"""

    title = models.CharField(max_length = 100)
    # author = models.ForeignKey("Author")
    author = models.ManyToManyField(Author)
    categories = models.ManyToManyField(BookCategory)

    def __str__(self):
        return self.title

class BookEdition(models.Model):
    """
    Wydanie okreslonej ksiazki
    """
    book = models.ForeignKey(Book)
    isbn = models.CharField(max_length = 17)
    publisher = models.ForeignKey("Publisher")

    def __str__(self):
        return "{book.title},{publisher.name}".format(book=self.book,
                                                      publisher=self.publisher)
COVER_TYPES = (
    ('soft','Soft'),
    ('hard','Hard'),
    # (wartosc w bazie, wartosc wyswietlania)
)

class BookItem(models.Model):
    """
    Konkretny egzemplarz
    """
    edition = models.ForeignKey(BookEdition)
    catalogue_number = models.CharField(max_length=30)
    cover_type = models.CharField(max_length=30,choices=COVER_TYPES)

    def __str__(self):
        return "{edition},{cover}".format(edition=self.edition, cover= self.get_cover_type_display())