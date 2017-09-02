from django.contrib import admin
from .models import Proponente

class ProponenteAdmin(admin.ModelAdmin):

    fields = ('nome', 'cpf', 'dtnascimento', 'email')

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self,request,obj=None):
        return False

admin.site.register(Proponente, ProponenteAdmin)
