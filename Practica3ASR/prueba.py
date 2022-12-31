from performance.app.device.performance_device.email_device import emaildevice
import rrdtool

pr = emaildevice()
rrdpath = '/home/hilda/Escritorio/ASR/Practica3/rrd_db/'


def prueba():
    ultima_actualizacion = rrdtool.lastupdate(rrdpath + "comunidadASRL.rrd")

    dato1 = ultima_actualizacion['ds']["CPUload"]
    dato2 = ultima_actualizacion['ds']["RAMload"]
    dato3 = ultima_actualizacion['ds']["NWload"]
    if dato1 > 25:
        pr.information_device_search('comunidadASRL 1 161 localhost', '-CPU')
    #if dato2 > 60:
    #    pr.information_device_search('comunidadASRL 1 161 localhost', '-RAM')
    #if dato3 > 195:
    #    pr.information_device_search('comunidadASRL 1 161 localhost', '-Trafico')


prueba()
