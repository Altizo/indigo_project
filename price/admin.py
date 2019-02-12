from django.contrib import admin
from .models import price_OffsetPress, price_LargeFormatPress, price_Design


class price_OffsetPressAdmin(admin.ModelAdmin):
    list_display = ('name', 'price1000', 'price2000', 'price5000')


admin.site.register(price_OffsetPress, price_OffsetPressAdmin)


class price_LargeFormatPressAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'cost')


admin.site.register(price_LargeFormatPress, price_LargeFormatPressAdmin)


class price_DesignAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')


admin.site.register(price_Design, price_DesignAdmin)
