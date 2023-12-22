import paho.mqtt.client as mqtt
import time

def on_message(subscriber, info_usuario, msg): #função 'callback', será chamada depois do recebimento de uma mensagem
    print("Mensagem recebida: " + str(msg.payload.decode("utf_8")))

url_broker = "mqtt.eclipseprojects.io"
subscriber = mqtt.Client("Computador_Central", transport="websockets") #Especificar que conexão será feita por meio
                                                                       #de websocket
# subscriber.tls_set("C:\\Users\\ThiagoGought\\Desktop\\CERTIFCADOS_SSL\\ISRG Root X1.crt")
# subscriber.tls_insecure_set(True)
subscriber.ws_set_options(path = "/mqtt", headers = None)
subscriber.connect(url_broker, port=80)

subscriber.subscribe("UMIDADE") #faz o subscribe para o tópico UMIDADE
subscriber.on_message = on_message #modifica o método on_message do cliente para o que nós criamos acima
subscriber.loop_forever(timeout=15) #criar um thread para lidar com o recebimento de mensagens
