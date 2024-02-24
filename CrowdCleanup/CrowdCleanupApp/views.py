# views.py
from django.shortcuts import render, redirect
from CrowdCleanupApp.models import Pin

def home(request):
    return render(request, 'home.html')

def report_litter(request):
    if request.method == 'POST':
        description = request.POST.get('description', '')
        latitude = request.POST.get('latitude', '')
        longitude = request.POST.get('longitude', '')
        zip_code = request.POST.get('zip_code', '')

        # Print the data in the command prompt
        print(f"Description: {description}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        print(f"Zip Code: {zip_code}")
        # Assuming you handle form submission here
        # Redirect to afterSubmit page after form submission
        return redirect('after_submit')  # Redirects to the URL with name 'after_submit'
    return render(request, 'report_litter.html')

def clean_litter(request):
    zip_code = request.GET.get('zip_code', None)
    
    # Use the zip code as needed in your view logic
    
    # Render the clean_litter template with any context data
    return render(request, 'clean_litter.html')  # Assuming you have a template named clean_litter.html

def pin_view(request, pin_id):
  pin = Pin.objects.get(id = pin_id)
  print(pin.image.url)
  return render(request, 'pin_view.html', {'pin' : pin})

def after_submit(request):
    return render(request, 'afterSubmit.html')
