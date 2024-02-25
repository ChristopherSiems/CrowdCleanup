# views.py
from django.shortcuts import render, redirect
from CrowdCleanupApp.models import Pin
from django.views.decorators.csrf import csrf_protect
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

@csrf_protect
def home(request):
    return render(request, 'home.html')

def report_litter(request):
  if request.method == 'POST':
    post = request.POST
    Pin.objects.create(lat = post['latitude'], long = post['longitude'], zipcode = post['zip_code'], description = post['description'], image = request.FILES.get('image'))
    return redirect('after_submit')  # Redirects to the URL with name 'after_submit'
  return render(request, 'report_litter.html')

@csrf_protect
def clean_litter(request):
    zip_code = request.POST.get('zip_code')
    pins_with_zip = Pin.objects.filter(zipcode=zip_code)  # Assuming Pin is your model representing litter pins
    json_pins = serializers.serialize('json', pins_with_zip)
    return render(request, 'clean_litter.html', {'pins_with_zip': pins_with_zip, 'zip_code' : zip_code, 'json_pins': json_pins})

@csrf_protect
def pin_view(request, pin_id):
    pin = Pin.objects.get(id=pin_id)
    if request.method == 'POST':
        pin.status = 'CLEANED'
        pin.save()
        print('heloo')
        return render(request, 'afterSubmit.html')
    return render(request, 'pin_view.html', {'pin': pin})

def after_submit(request):
    return render(request, 'afterSubmit.html')
