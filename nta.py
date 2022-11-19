
import webbrowser
import dpkt
import socket
import pygeoip
from requests import get
from features import *

ip = get('https://api.ipify.org').content.decode('utf8')
##print('My public IP address is: {}'.format(ip))
gi = pygeoip.GeoIP('GeoLiteCity.dat')
def retKML(dstip, ips):
    dst = gi.record_by_name(dstip)
    ##print(ip)
    src = gi.record_by_name(ip)
    try:
        dstlongitude = dst['longitude']
        dstlatitude = dst['latitude']
        dstcity = dst['city']
        dstcnt = dst['country_name']

        srclongitude = src['longitude']
        srclatitude = src['latitude']
        kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<extrude>2</extrude>\n'
            '<tessellate>2</tessellate>\n'
            '<styleUrl>#transBluePoly</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        )%(dstcnt, dstlongitude, dstlatitude, srclongitude, srclatitude)
        return kml
    except:
        return ''

def plotIPs(pcap):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            KML = retKML(dst, src)
            kmlPts = kmlPts + KML
        except:
            pass
    return kmlPts


def main():
    f = open('wire5.pcap','rb')
    pcap = dpkt.pcap.Reader(f)
    kmlheader = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2%22%3E/n<Document>\n'\
    '<Style id="transBluePoly">' \
                '<LineStyle>' \
                '<width>1.5</width>' \
                '<color>501400E6</color>' \
                '</LineStyle>' \
                '</Style>'
    kmlfooter = '</Document>\n</kml>\n'
    kmldoc=kmlheader+plotIPs(pcap)+kmlfooter
    kmldoc = kmldoc.replace("2.2%22%3E",'2.2">')
    #print(kmldoc)
    if 'United States' in kmldoc:
        print("valid")
    with open("output.kml",'w+') as file:
        file.write(kmldoc)

        file.close()
    sleep(5)
    talk("scaning completed, opening google maps")
    talk("this are the locations where your network is connected sir")

    # webbrowser.open("output.kml")
    webbrowser.open("https://www.google.com/maps/d/edit?mid=1F45Zx02mwapWz7WQAm2tL-yPAYskhh78&ll=8.424383440500002%2C0&z=2")


