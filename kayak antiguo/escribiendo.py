import paho.mqtt.client as mqtt #import the client1
broker_address="192.168.137.247" 
#broker_address="iot.eclipse.org"
print("creando una nueva instancia")
client = mqtt.Client("KAYAK") #create new instance
print("connectandome al broker")
client.connect(broker_address) #connect to broker
print("Subscribiendome al topico")
client.subscribe("central/datos")
while True:
    
    print("publicando")
    client.publish("central/datos","prueba")
