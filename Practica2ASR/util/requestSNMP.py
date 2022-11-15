#Se reciben los paramentos correspondientes para hacer las peticiones get
from pysnmp.hlapi import *
def request(comunidad,SNMPv, puerto,ip,OID):
    iterator = getCmd(
    SnmpEngine(),
    CommunityData(comunidad, mpModel=0),
    UdpTransportTarget((ip, puerto)),
    ContextData(),
    ObjectType(ObjectIdentity(OID))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)
        return('ERROR')

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        return('ERROR')

    else:
        for varBind in varBinds:
            aux=str(varBind).split("=")
            return(aux[1])