from django.contrib import admin

from .models import *

from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "is_reviewer", "is_staff")
    list_filter = ("is_reviewer", "is_staff")
    search_fields = ("email", "first_name", "last_name")

# admin.site.register(CustomUser)
admin.site.register(Item)
admin.site.register(PurchaseRequest)
admin.site.register(Supplier)
admin.site.register(PurchaseOrder)
admin.site.register(DeliveredItems)
admin.site.register(RequisitionIssueSlip)
admin.site.register(FundCluster)
admin.site.register(Office)