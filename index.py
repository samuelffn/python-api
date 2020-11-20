import numpy as np
import json
import math

##PEGAR DADOS JSON (OK)
with open('rows.json') as f: data = json.load(f)

#input = ['39.0401813', '-77.0496475']

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d


def bestRoute(lat, long):
    dataFormated = []
    
    ##FORMARTAR OS DADOS - NOME - LATITUDE - LONGITUDE - DISTANCE EM KM (OK)
    for line in data['data']: 
        dataFormated.append([line[18], line[11], line[12], distance((float(lat), float(long)), (float(line[11]), float(line[12])))])

    f.close()

    ##ORDENAR OS DADOS DO ARRAY PELA MENOR DISTANCIA
    dataFormated = sorted(dataFormated, key=lambda parking: parking[3] , reverse=True)

    ##SAIDA O MELHOR ESTACIONAMENTO POR DISTANCIA
    #print(dataFormated[0])
    return { "data": dataFormated[0] }
