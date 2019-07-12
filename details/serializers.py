from rest_framework import serializers

from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'full_name', 'flat_no', 'phone1', 'phone2',
                  'email', 'status', 'active', 'staff', 'admin', 'corpus_due', 'corpus_due_date',
                  'membership_due', 'membership_due_date', 'legal_charges_due', 'legal_charges_due_date',
                  'consumer_due', 'consumer_due_date', 'maintenance_due', 'maintenance_date'
                  )
