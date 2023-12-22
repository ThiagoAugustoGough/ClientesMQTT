import paho.mqtt.client as mqtt
import time

def on_message(subscriber, info_usuario, msg): #função 'callback', será chamada depois do recebimento de uma mensagem
    print("Mensagem recebida: " + str(msg.payload.decode("utf_8")))

url_broker = "mqtt.eclipseprojects.io"
subscriber = mqtt.Client("Computador_Central") 
subscriber.connect(url_broker)

subscriber.subscribe("UMIDADE") #faz o subscribe para o tópico UMIDADE
subscriber.on_message = on_message #modifica o método on_message do cliente para o que nós criamos acima
subscriber.loop_forever(timeout=15) #criar um thread para lidar com o recebimento de mensagens
