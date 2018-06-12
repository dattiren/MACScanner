from django.shortcuts import render
from scanner.models import *
import csv
from io import TextIOWrapper, StringIO
from scapy.layers.l2 import *
from datetime import datetime
from django.views.generic import TemplateView
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

def get_address():
    ip = '133.14.206.*'
    print('start: {}'.format(datetime.now().strftime('%Y/%m/%d %H:%M:%S')))
    result, nonresult = arping(ip, timeout=1, verbose=0)
    maclist=[]
    for send_packet, recieve_packet in result:
        macaddress=recieve_packet[ARP].hwsrc.replace(":","")
        bendar_num=macaddress[:6]
        print('MAC Address: {}'.format(
            macaddress,  # MACアドレス
            # recieve_packet[ARP].psrc   # IPアドレス
        )
        )
        if Organization.Objects.filter(assignment = bendar_num).exists():
            maclist.append()
        else:
            print("no Macthed")
    print('end  : {}'.format(datetime.now().strftime('%Y/%m/%d %H:%M:%S')))
    if len(maclist)==0:
        return "Np Matching"
    else:
        return maclist

class ScannerListView(TemplateView):
    template_name = "scanner/scanner_list.html"

    def get(self, request, *args, **kwargs):
        context = super(ScannerListView, self).get_context_data(**kwargs)
        context['scanner_list'] = get_address()
        return render(self.request, self.template_name, context)

