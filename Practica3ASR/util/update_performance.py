import time
import rrdtool
from requestSNMP import request

rrdpath = '/home/hilda/Escritorio/ASR/Practica3/rrd_db/'

processors = ['196608', '196609']

while 1:
    CPU_load = 0
    for pro in processors:
        single_cpu_load = int(request('comunidadASRL', '1', '161', 'localhost', '1.3.6.1.2.1.25.3.3.1.2.' + pro))
        CPU_load += int(single_cpu_load)

    ram_free = int(request('comunidadASRL', '1', '161', 'localhost', '1.3.6.1.4.1.2021.4.11.0'))
    ram_total = int(request('comunidadASRL', '1', '161', 'localhost', '1.3.6.1.4.1.2021.4.5.0'))
    ram_load = ram_total - ram_free
    ram_total_load = (ram_load / ram_total) * 100

    NW_load = 0
    #TNW_OID = ['1.3.6.1.2.1.31.1.1.1.2.1', '1.3.6.1.2.1.31.1.1.1.2.2', '1.3.6.1.2.1.31.1.1.1.3.1',
    #           '1.3.6.1.2.1.31.1.1.1.3.2', '1.3.6.1.2.1.31.1.1.1.4.1', '1.3.6.1.2.1.31.1.1.1.4.2',
    #           '1.3.6.1.2.1.31.1.1.1.5.1', '1.3.6.1.2.1.31.1.1.1.5.2', '1.3.6.1.2.1.5.1.0']
    TNW_OID = ['1.3.6.1.2.1.2.2.1.10.1', '1.3.6.1.2.1.2.2.1.10.2', '1.3.6.1.2.1.2.2.1.16.1', '1.3.6.1.2.1.2.2.1.16.2']
    for oid in TNW_OID:
        single_traficc = int(request('comunidadASRL', '1', '161', 'localhost', oid))
        NW_load += int(single_traficc)

    value = "N:" + str(CPU_load/2) + ":" + str(ram_total_load) + ":" + str(NW_load/1048576)
    print(value)

    rrdtool.update(rrdpath + 'comunidadASRL.rrd', value)
    time.sleep(5)
