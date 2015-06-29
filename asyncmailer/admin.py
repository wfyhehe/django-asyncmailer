from django.contrib import admin
from asyncmailer.models import Provider, EmailTemplate, DeferredMail

# Register your models here.
admin.site.register(Provider)
admin.site.register(EmailTemplate)
admin.site.register(DeferredMail)