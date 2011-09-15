from django.contrib import admin
from apps.rocket.models import Client, Brand, Campaign, RefererBlock, \
    Step, Decision, Customer, Session


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'total_units',)


class BrandAdmin(admin.ModelAdmin):
    pass


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'begins', 'ends', 'active',)


class RefererBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'campaign', 'match',)


class StepAdmin(admin.ModelAdmin):
    list_display = ('id', 'campaign', 'name', 'sort',)


class DecisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'step', 'goto', 'rules', 'match_all',)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'gender',)


class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'last_step',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(RefererBlock, RefererBlockAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Decision, DecisionAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Session, SessionAdmin)
