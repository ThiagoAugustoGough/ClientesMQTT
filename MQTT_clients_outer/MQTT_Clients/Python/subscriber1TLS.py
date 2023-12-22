import paho.mqtt.client as mqtt
import time

def on_message(subscriber, info_usuario, msg): #função 'callback', será chamada depois do recebimento de uma mensagem
    print("Mensagem recebida: " + str(msg.payload.decode("utf_8")))

url_broker = "mqtt.eclipseprojects.io"
subscriber = mqtt.Client("Computador_Central")
subscriber.tls_set("C:\\Users\\ThiagoGought\\Desktop\\CERTIFCADOS_SSL\\ISRG Root X1.crt")
#subscriber.tls_insecure_set(True)
subscriber.connect(url_broker, port=8883)

subscriber.subscribe("UMIDADE") #faz o subscribe para o tópico UMIDADE
subscriber.on_message = on_message #modifica o método on_message do cliente para o que nós criamos acima
try:
    subscriber.loop_forever(timeout=30) #criar um thread para lidar com o recebimento de mensagens
except KeyboardInterrupt:
    exit()
