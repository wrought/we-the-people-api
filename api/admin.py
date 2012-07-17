from api.models import Petition, Signature
from django.contrib import admin

class PetitionAdmin(admin.ModelAdmin):
    list_display = ('pid', 'url', 'whurl', 'description', 'created_at', 'issues', 'signature_count', 'signatures_needed')

admin.site.register(Petition, PetitionAdmin)

class SignatureAdmin(admin.ModelAdmin):
    list_display = ('sig_num', 'sig_date', 'first_name', 'last_initial', 'location_city', 'location_state', 'lat', 'lng', 'url')

admin.site.register(Signature, SignatureAdmin)
