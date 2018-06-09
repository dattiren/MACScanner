from django.shortcuts import render
from scanner.models import Organization, Machine
import csv
from io import TextIOWrapper, StringIO
import code
# Create your views here.

def upload(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file)
        # csv_file = csv.reader(form_data)
        # csv_file = open(request.FILES['csv'].file, 'r', newline='')
        # reader = csv.reader(csv_file)
        reader = csv.reader(form_data)
        for line in reader:
            org, created = Organization.objects.get_or_create(assignment=line[1])
            org.registry = line[0]
            org.assignment = line[1]
            org.organization = line[2]
            org.organization_address = line[3]
            org.save()

        return render(request, 'upload.html')
    else:
        return render(request, 'upload.html')
