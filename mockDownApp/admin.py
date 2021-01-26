from django.contrib import admin
from mockDownApp import models


# Register your models here.


from mockDownApp.models import YesNoBar


admin.site.site_header="mockDown your mail list"
admin.site.site_title="Admin"

@admin.register(models.YesNoBar)
class YesNoBarAdmin(admin.ModelAdmin):

    # date_hierarchy = 'created'
    # search_fields = ['title', 'location',]
    list_display = ('id','user','name','category','yes_button_text','no_button_text')


    # list_filter = ('status',)


# @admin.register(models.Announced_lga_result)
# class Announced_lga_resultAdmin(admin.ModelAdmin):
#     list_display = ('id','lga_name','party_abbreviation','party_score','date_entered','user_ip_address',)

