from django.db import models


class Product(models.Model):

    title = models.CharField(max_length=250)
    price = models.IntegerField()
    category = models.ManyToManyField('Category', max_length=10, verbose_name='product')
    slug = models.SlugField(max_length=250)
    is_active = models.BooleanField(default=True)
    on_delete = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __repr__(self):
        return f'{self.title}({self.category})'

    class Meta:
        ordering = ('date', )
        

class Category(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __repr__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('title', )
