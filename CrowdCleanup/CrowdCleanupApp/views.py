# views.py
from django.shortcuts import render, redirect
from CrowdCleanupApp.models import Pin

def home(request):
    return render(request, 'home.html')

def report_litter(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        image = request.FILES.get('image')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        zip_code = request.POST.get('zip_code')

        # Print the submitted information in the command prompt
        print("Description:", description)
        print("Latitude:", latitude)
        print("Longitude:", longitude)
        print("Zip Code:", zip_code)
        return redirect('after_submit')  # Redirects to the URL with name 'after_submit'
    return render(request, 'report_litter.html')

def clean_litter(request):
    # Logic for cleaning up litter
    return render(request, 'clean_litter.html')  # Assuming you have a template named clean_litter.html

def pin_view(request, pin_id):
  pin = Pin.objects.get(id = pin_id)
  print(pin.image.url)
  return render(request, 'pin_view.html', {'pin' : pin})

def after_submit(request):
    return render(request, 'afterSubmit.html')
