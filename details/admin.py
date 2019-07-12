from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import *
from .models import *

admin.site.site_header = "Admin Panel"


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'full_name', 'status', 'admin',)
    list_filter = ('admin', 'status')
    fieldsets = (
        (None, {'fields': ('username', 'status', 'password', 'flat_no')}),
        ('Personal info', {'fields': ('full_name', 'phone1', 'phone2', 'email',)}),
        ('Dues info', {'fields': ('corpus_due', 'corpus_due_date', 'membership_due', 'membership_due_date',
                                  'legal_charges_due', 'legal_charges_due_date', 'consumer_due',
                                  'consumer_due_date', 'maintenance_due', 'maintenance_due_date')}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'status', 'password1', 'password2')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
