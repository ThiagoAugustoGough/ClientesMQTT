const mqtt = require("mqtt");

var mqttClient;

function conectarAoBroker() {
    const IdCliente = "termometro";

    // Estabelecendo o URL do broker
    const URLBroker = "https://mqtt.eclipseprojects.io/";

    const opcoesConexao = {
        keepalive: 60,
        clientId: "termometro",
        protocolId: "MQTT",
        clean: true, //Conexao re-inicializada toda vez que o programa rodar
        reconnectPeriod: 1000,
        connectTimeout: 30 * 1000,
        port: 1883
    };

    //Conectando ao broker
    mqttClient = mqtt.connect(URLBroker);

    //Criando callbacks, funções que serão chamadas após o evento acontecer

    mqttClient.on("error", (err) => {
        console.log("Erro: ", err);
        mqttClient.end();
    });

    mqttClient.on("reconnect", () => {
        console.log("Reconnectando...");
    });

    mqttClient.on("connect", () => {
        console.log("Cliente Conectado: " + IdCliente);
    });

    mqttClient.on("message", (topic, message, packet) => {
        console.log(
            "Mensagem recebida: " + message.toString() + "\nNo topico: " + topic
        );
    });
}

function publishMessage(topic, msg) {
    console.log(`Entregando no topico: ${topic}, Mensagem: ${msg}`);
    mqttClient.publish(topic, msg, {
        qos: 1,
        retain: false,
    });
}

conectarAoBroker();

// for (let i = 1; i <= 15; i++) {
    let msg = ((Math.random() * 16) + 10).toString();
    publishMessage("temperatura", msg);
//   }

process.exit();