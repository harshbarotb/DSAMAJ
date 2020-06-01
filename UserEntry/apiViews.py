from django.core import serializers
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def getFamilycode(request):
    familyCode = FamilyCode.objects.filter(id=request.POST.get('id',''))
    familyCode_obj = serializers.serialize('001',familyCode)
    return JsonResponse(familyCode_obj, safe=False)