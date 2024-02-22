from django.contrib import admin
from.models import Product, Contact, TopRanking,Checkout


# Register your models here.

#path("",views.index,name='index')
#from.import views


# class AfxlllStore(admin.TabularInline):
#     model=OrderItems
# class OrderAdmin(admin.ModelAdmin):
#     inlines=[AfxlllStore]


admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(TopRanking)
admin.site.register(Checkout)
# admin.site.register(OrderItems)
