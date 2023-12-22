const mqtt = require("mqtt");
const fs = require("fs");

const CERT = fs.readFileSync("C:\\Users\\ThiagoGought\\Desktop\\CERTIFCADOS_SSL\\ISRG Root X1.crt");

const connectOptions = {
    port: 443,
    protocol: 'wss',
    path: '/mqtt',
    clientId: 'ar_condicionado',
    cert : CERT
};

const cliente = mqtt.connect("ws://mqtt.eclipseprojects.io", connectOptions);

cliente.on("connect", () => {
    console.log("Cliente conectado!");
    cliente.subscribe("temperatura", (err) => {
        if (!err) {
            console.log("Cliente inscrito no tópico temperatura");
        } else {
            console.log("Falha ao inscrever no tópico temperatura");
        }
    });
});

cliente.on("message", (topic, message) => {
    console.log("Mesagem recebida: " + message.toString() + " no tópico " + topic);
});