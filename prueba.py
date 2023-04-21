import io
import pynmea2
import serial
"""
import paho.mqtt.client as mqtt #import the client1
broker_address="192.168.137.247" 
#broker_address="iot.eclipse.org"
print("creando una nueva instancia")
client = mqtt.Client("KAYAK") #create new instance
print("connectandome al broker")
client.connect(broker_address) #connect to broker
print("Subscribiendome al topico")
client.subscribe("central/datos")
"""
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

while 1:
    try:
        line = sio.readline()
        msg = pynmea2.parse(line)
        #print(repr(msg))
        aux=str(type(msg)).split(".")[3].split("'")[0]
        if aux=="MTW":
            temp=str(msg.temperature)
            unit=str(msg.units)
            aux="MTW,"+temp+unit
            #client.publish("central/datos",aux)
            print(aux)
        elif aux=="DPT":
            profundidad=str(msg.depth)
            aux="DPT,"+profundidad
            print(aux)
            #client.publish("central/datos",aux)
        elif aux=="RMC":
            tiempo=str(msg.timestamp)
            latitud=str(msg.lat)
            longitud=str(msg.lon)
            velocidad=str(msg.spd_over_grnd)
            aux="RMC,"+tiempo+","+latitud+","+longitud+","+velocidad
            print(aux)
            #client.publish("central/datos",aux)
    except serial.SerialException as e:
        print("---")
        continue
    except pynmea2.ParseError as e:
        print("____")
        continue
