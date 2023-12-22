import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

url_broker = "mqtt.eclipseprojects.io" #Usaremos este broker de teste, provido pelo Eclipse,
                                       #assim não precisamos programar o nosso ainda

client = mqtt.Client("Sensor_TAS_1") #Usando o método 'Client' para criar e atribuir um 'ID' ao nosso sensor
client.connect(url_broker) #Conectando ao broker público do Eclipse
message_counter = 0

while message_counter <= 25:
    num_aleatorio = uniform(0, -40) #gerar um número aleatorio entre 0 e -40, representando a tensão do solo
    client.publish("UMIDADE", num_aleatorio) #enviar mensagem, especificando como o primeiro parametro
                                             # o topico e o segundo o payload/msg

    print("Mensagem " + str(num_aleatorio) + " Enviada para o broker no topico UMIDADE")
    message_counter += 1
    time.sleep(1) #espera um segundo antes de gerar a próxima medida e publicar a mensagem