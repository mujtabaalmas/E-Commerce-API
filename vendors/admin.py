from django.contrib import admin
from vendors.models import Vendors
# Register your models here.

#admin.site.register(Users)

class VendorAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'verified', 'joined_date',)

admin.site.register(Vendors, VendorAdmin)


