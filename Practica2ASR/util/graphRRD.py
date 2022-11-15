
import rrdtool
import time

def graph_rrd(time_init, time_end, device, title, index, lvertical, var):


    ret = rrdtool.graphv("docs/" + device + "-" + str(index) + ".png",
                         "--start", time_init,
                         "--end", time_end,
                         "--vertical-label=" + lvertical,
                         "--title=" + title,  # titulo
                         "DEF:sEntrada=util/" + device + ".rrd:" + var + ":AVERAGE",
                         "LINE3:sEntrada#FF0000:" + title,
                         )
    #print(ret)
