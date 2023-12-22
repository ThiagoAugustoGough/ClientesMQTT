const mqtt = require("mqtt");
const client = mqtt.connect("https://mqtt.eclipseprojects.io/"); //conectando assim que cliente é criado

client.on("connect", () => {
  console.log("Cliente conectado!");
  client.subscribe("temperatura", (err) => {
    if (!err) {
      console.log("Cliente subscrito ao topico: temperatura");
      publicarMensagens();
    }
  });
});

const publicarMensagens = () => {
  const intervalId = setInterval(() => {
    publicarTemperatura(intervalId);
  }, 500);
};

let msg_counter = 1;
const publicarTemperatura = (intervalId) => {
  
  if (msg_counter <= 15) {
    let msg = ((Math.random() * 16) + 10).toString();
    client.publish("temperatura", msg);
    console.log("Mensagem enviada");
    msg_counter++;
  } else {
    clearInterval(intervalId); // Parar o intervalo quando 15 mensagens forem enviadas
    process.exit(0);
  }
};

