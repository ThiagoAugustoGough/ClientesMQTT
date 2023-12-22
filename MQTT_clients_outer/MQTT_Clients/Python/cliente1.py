import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

url_broker = "mqtt.eclipseprojects.io" #Usaremos este broker de teste, provido pelo Eclipse,
                                       #assim não precisamos programar o nosso ainda

client = mqtt.Client("Nome/id_Cliente", userdata="thiago") #Usando o método 'Client' para criar e descrever o comportamento de nosso cliente
client.connect(url_broker, 8883)

while True:
    num_aleatorio = uniform(20.0, 21.0) #gerar um número aleatorio entre 20.0 e 21.0, representando uma temperatura
    client.publish("TEMPERATURA", num_aleatorio) #enviar mensagem, especificando como o primeiro parametro o topico e o segundo o payload/msg
    print("Mensagem " + str(num_aleatorio) + " Enviada para o broker no topico TEMPERATURA")
    time.sleep(1) #espera um segundo antes de gerar a próxima temperatura e publicar a mensagem