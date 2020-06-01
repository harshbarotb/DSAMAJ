import django_filters
from UserEntry.models import *


class HeadPersonFilter(django_filters.FilterSet):
    class Meta:
        model = FamilyHead
        fields = {
            'Zone_Name': ['icontains'],
            'Native_City': ['icontains'],
            'Town': ['icontains'],
            'HeadPerson_Of_Family': ['exact'],
            'F_Code': ['exact']
        }
