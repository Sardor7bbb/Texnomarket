
from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    massage = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


class TeamModel(models.Model):
    full_name = models.CharField(max_length=128)
    job = models.CharField(max_length=128)
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'feedback'
        verbose_name_plural = 'feedbacks'


class AboutModel(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='about/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

