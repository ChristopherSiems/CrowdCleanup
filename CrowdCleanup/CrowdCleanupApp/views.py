# views.py
from django.shortcuts import render, redirect
from CrowdCleanupApp.models import Pin

def home(request):
    return render(request, 'home.html')

def report_litter(request):
  if request.method == 'POST':
    post = request.POST
    Pin.objects.create(lat = post['latitude'], long = post['longitude'], zipcode = post['zip_code'], description = post['description'], image = request.FILES.get('image'))
    return redirect('after_submit')  # Redirects to the URL with name 'after_submit'
  return render(request, 'report_litter.html')

def clean_litter(request):
    zip_code = request.GET.get('zip')
    if zip_code:
        pins_with_zip = Pin.objects.filter(zipcode=zip_code)
        return render(request, 'clean_litter.html', {'zipcode': zip_code, 'pins_with_zip': pins_with_zip})
    else:
        return render(request, 'clean_litter.html')
    
def pin_view(request, pin_id):
    pin = Pin.objects.get(id=pin_id)
    print(pin.image.url)
    return render(request, 'pin_view.html', {'pin': pin})

def after_submit(request):
    return render(request, 'afterSubmit.html')
