from api.models import Petition, Signature
from django.contrib import admin

class PetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'pid', 'url')

admin.site.register(Petition, PetitionAdmin)

class SignatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'sid', 'petition')

admin.site.register(Signature, SignatureAdmin)
