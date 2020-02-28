from scapy.all import IP, sniff
from scapy.layers import http

def tcp_ayikla(paket):
    if not paket.haslayer(http.HTTPRequest):
        return

    http_katmani = paket.getlayer(http.HTTPRequest)


    ip_katmani = paket.getlayer(IP)
    print '\n{0[src]} IP adresinden {1[Method]} {1[Host]}{1[Path]} sitesine ziyaret\n'.format(ip_katmani.fields, http_katmani.fields)


sniff(filter='tcp', prn=tcp_ayikla)
