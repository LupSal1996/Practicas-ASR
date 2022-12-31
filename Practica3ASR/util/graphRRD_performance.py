import sys
import rrdtool
import time
import datetime
# from  Notify import send_alert_attached
import time
rrdpath = 'rrd_db/'
imgpath = 'docs/'

def graph_rrd(init, end, community, title, i, vertical, var, ll, ul, var_desc, umbrales):

    ret = rrdtool.graphv( imgpath+community+"-"+i+".png",
                     "--start",str(init),
                     "--end",str(end),
                     "--vertical-label="+vertical,
                    '--lower-limit', ll,
                    '--upper-limit', ul,
                    "--title="+title,
                    "DEF:carga="+rrdpath+community+".rrd:"+var+":AVERAGE",
                     "VDEF:cargaMAX=carga,MAXIMUM",
                     "VDEF:cargaMIN=carga,MINIMUM",
                     "VDEF:cargaSTDEV=carga,STDEV",
                     "VDEF:cargaLAST=carga,LAST",
                     "CDEF:umbral1=carga,"+umbrales[0]+",LT,0,carga,IF",
                     "CDEF:umbral2=carga,"+umbrales[1]+",LT,0,carga,IF",
                     "CDEF:umbral3=carga,"+umbrales[2]+",LT,0,carga,IF",
                     "AREA:carga#24B015:"+var_desc,
                     "AREA:umbral1#E7DD1E:Mayor de "+umbrales[0],
                     "AREA:umbral2#EC7C:Mayor de "+umbrales[1],
                     "AREA:umbral3#C32210:Mayor de "+umbrales[2],
                     "HRULE:"+umbrales[0]+"#1EC2CB:Umbral "+umbrales[0],
                     "HRULE:"+umbrales[1]+"#E485EC:Umbral "+umbrales[1],
                     "HRULE:"+umbrales[2]+"#E421D1:Umbral "+umbrales[2],
                     "PRINT:cargaLAST:%6.2lf",
                     "GPRINT:cargaMIN:%6.2lf %SMIN",
                     "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                     "GPRINT:cargaLAST:%6.2lf %SLAST" )
    print (ret)