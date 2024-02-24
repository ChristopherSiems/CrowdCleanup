# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def report_litter(request):
    # Logic for reporting litter
    return render(request, 'report_litter.html')  # Assuming you have a template named report_litter.html

def clean_litter(request):
    # Logic for cleaning up litter
    return render(request, 'clean_litter.html')  # Assuming you have a template named clean_litter.html

def pin_view(request):
  return render(request, 'pin_view.html')
