import time
import rrdtool
from requestSNMP import request

while 1:
    interf_G = int(
        request('comunidadASRL', '1', '161', 'localhost', '1.3.6.1.2.1.2.2.1.17.1'))

    pc_IP = int(
        request('comunidadLuisASR', '1', '161', '192.168.158.172', '1.3.6.1.2.1.4.10.0'))

    ms_ICMP = int(
        request('comunidadLuisASR', '1', '161', '192.168.158.172', '1.3.6.1.2.1.5.1.0'))

    sg_TCP = int(
        request('comunidadLuisASR', '1', '161', '192.168.158.172', '1.3.6.1.2.1.6.12.0'))

    dg_UDP = int(
        request('comunidadLuisASR', '1', '161', '192.168.158.172', '1.3.6.1.2.1.7.4.0'))

    valor = "N:" + str(interf_G) + ":" + str(pc_IP) + ":" + str(ms_ICMP) + ":" + str(sg_TCP) + ":" + str(dg_UDP)
    print(valor)

    rrdtool.update('comunidadLuisASR.rrd', valor)
    rrdtool.dump('comunidadLuisASR.rrd','comunidadLuisASR.xml')
    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)