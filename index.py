from subscriber import client
from publisher import sensorPublisher

topicos = {
    "1": "topico/Velocidade",
    "2": "topico/Temperatura",
    "3": "topico/Humidade",
}

def clientBuilder():
  print("INICIANDO CLIENTE")
  while True:
    input("Pressione Enter para uma nova inscrição em topico")
    topico = input("Digite 1 (Velocidade), 2 (Temperatura) ou 3 (Humidade)")
    if (topico == "0"): break
    print(f"conectando em: {topicos[topico]}")
    client.subscribe(topicos[topico])
    client.loop_forever()


  client.disconnect()

def sensorBuilder():
  while True:
    input("Pressione Enter para um novo sensor")
    topico = input("Digite 1 (Velocidade), 2 (Temperatura) ou 3 (Humidade)")
    if (topico == "0"): break
    sensorPublisher.publish(topicos[topico], f"Sensor de {topicos[topico].split("/")[1]}")
    print(f"conectando em: {topicos[topico]}")

  sensorPublisher.disconnect()

def mainApp():
  opcao = input("Selecione o tipo de aplicação\n1 (cliente) 2 (sensor)")
  if opcao == "1": clientBuilder()
  elif opcao == "2": sensorBuilder()
  else: mainApp()

if __name__ == "__main__":
  mainApp()