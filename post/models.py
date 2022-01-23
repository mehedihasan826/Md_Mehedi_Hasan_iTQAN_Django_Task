from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    group = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name + ' | ' + str(self.group)
