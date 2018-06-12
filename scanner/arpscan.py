from scapy.layers.l2 import *
from datetime import datetime
from scanner.models import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')


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
            print(maclist)
        else:
            print("no Macthed")

    print(nonresult)
    print('end  : {}'.format(datetime.now().strftime('%Y/%m/%d %H:%M:%S')))


if __name__ == '__main__':
    get_address()
