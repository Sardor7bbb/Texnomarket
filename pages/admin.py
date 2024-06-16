from django.contrib import admin

from pages.models import ContactModel, AboutModel, TeamModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at',)
    search_fields = ('name', 'email', 'subject',)
    list_filter = ('email', 'created_at',)


@admin.register(TeamModel)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ['job', 'created_at']
    search_fields = ['job']
    list_filter = ['created_at', 'job']


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['text', 'image',]
    search_fields = ['text',]
    list_filter = ['created_at', 'text']

