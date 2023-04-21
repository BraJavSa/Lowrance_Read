import paho.mqtt.client as mqtt
from dronekit import connect
from time import sleep
from datetime import datetime
vehicle = connect('tcp:192.168.43.172:5760', wait_ready=True)
print("good")
"""
broker_address="192.168.1.10" 
client = mqtt.Client("KAYAK") 
print("connectandome al broker")
client.connect(broker_address) 
print("Listo")
while True:
    loca=str(vehicle.location.global_frame).split(":")
    attitude=str(vehicle.attitude).split(":")
    velocidad=vehicle.velocity
    now = str(datetime.now()).split(" ")
    hora=now[1].split(".")
    heading=str(vehicle.heading)
    datos= str(loca[1]) +" "+"H: "+heading+" "+str(attitude[1])+" v: "+ str(velocidad)+" "+str(hora[0])
    print(datos)
    print("  ")
    client.publish("central/kayak",datos)
    fic = open("informacion.txt", "a")
    fic.write(datos)
    fic.write("\n")
    fic.close()
    sleep(1)


"""
