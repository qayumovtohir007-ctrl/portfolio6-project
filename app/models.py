from django.db import models


class Portfolio(models.Model):
    image = models.ImageField()
    title = models.CharField()
    link = models.CharField()
    text = models.TextField(null=True, blank=True) # data kiritish majburiy emas

    def __str__(self):
        return self.title



class Contact(models.Model):
    name = models.CharField()
    email = models.EmailField()
    subject = models.CharField()
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name



class Service(models.Model):
    title = models.CharField()
    text = models.CharField()

    def __str__(self):
        return self.title