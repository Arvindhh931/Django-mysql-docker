from django.shortcuts import render
from login.models import Employee
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def register(request):
    try:
        if request.method == 'POST':           
            data = json.loads(request.body)
            name_ = data.get('name')
            department_ = data.get('department')
            salary_ = data.get('salary')
            new_record = Employee(name=name_,department=name_,salary=salary_)
            new_record.save()
            return render(request,'successfully added employee record')
    except json.JSONDecodeError as e:
        # Handle JSON decoding errors
        return JsonResponse({'error': 'there is some error'}, status=400)


