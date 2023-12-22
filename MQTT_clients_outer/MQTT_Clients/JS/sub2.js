const mqtt = require("mqtt");
const cliente = mqtt.connect("https://mqtt.eclipseprojects.io/");

cliente.on("connect", () => {
    cliente.subscribe("temperatura", (err) => {
        if(!err){
            console.log("Cliente inscrito no tópico temperatura");
        }else{
            console.log("Falha ao inscrever no tópico temperatura");
        }
    });
});

cliente.on("message", (topic, message) => {
    console.log("Mesagem recebida: " + message.toString() + " no tópico " + topic);
});