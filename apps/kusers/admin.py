from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Kuser

def photo(obj):
    if obj.photo:
        html = '<img src="'+ obj.photo.url +'" class="adminavatar">'
    else:
        html = '<span class="nophoto">No Photo</span>'
    return html

# Admin Inline que aparece en los User, con su KUser relacionado
class KuserInline(admin.StackedInline):
    model = Kuser
    can_delete = False

# Admin de los User, alterado para poner foto y los KuserInlines
class KuserAdmin(UserAdmin):

    list_display = UserAdmin.list_display + ('photo_admin',)
    inlines = (KuserInline,)

    def photo_admin(self, obj):
        return photo(obj.kuser)

    class Media:
        css = {
            "all":("css/propio.css",)
        }

    photo_admin.allow_tags = True
    photo_admin.short_description = 'Fotografia'

# Admin de los Kuser
class OtherKuserAdmin(admin.ModelAdmin):

    list_display = ('user','cargo', 'departamento', 'photo_admin','customer')

    def photo_admin(self, obj):
        return photo(obj)

    photo_admin.allow_tags = True
    photo_admin.short_description = 'Fotografia'

    class Media:
        css = {
            "all":("css/propio.css",)
        }

admin.site.unregister(User)
admin.site.register(User, KuserAdmin)

admin.site.register(Kuser, OtherKuserAdmin)
