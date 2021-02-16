# Ambiente Inteligente
- Linguagem utilizada: Python
- Uso de multicast para identificação de novos objetos
- Comunicação TCP entre objetos e gateway
- Comunicação TCP como uso de protocol buffers entre aplicação e gateway
- Suporte a comandos
- Bibliotecas utilizadas:
  - Socket;
  - Threading;
  - Time;
  - Struct;
  - Protocol Buffers.

A intenção do projeto é ter uma aplicação (que simulamos no terminal), esta se conecta ao gateway. Essa conexão ocorre via TCP usando Protocol Buffers. 
Já o Gateway realiza a descoberta de objetos inteligentes via multicast. Ocorre, posteriormente, a conexão do Gateway com esses objetos.
A aplicação pode solicitar status desses objetos e solicitar modificação desses status. Além disso, um dos objetos do projeto deve enviar periodicamente uma atualização ao Gateway do seu status e algum atributo.
Resumindo, é uma simulação de projeto envolvendo IoT. 

## Objetos Usados
- Lâmpada (LAMP.PY)
  Status: ligado / desligado
  ENVIO DO STATUS QUANDO SOLICITADO
- BORRIFADOR (SPRINKLER.PY)
  STATUS: LIGADO / DESLIGADO
  ENVIO DO STATUS QUANDO SOLICITADO
- AR CONDICIONADO (AC.PY)
  STATUS: LIGADO / DESLIGADO
  TEMPERATURA
  ENVIO periodico DE SUA TEMPERATURA E STATUS

Essas funções que representam os objetos se encontram dentro da pasta objects.

## Lógica Multicast
Funcionalidade de descoberta de objetos inteligentes, usando comunicação em grupo (multicast).
- GATEWAY ENVIA O IP E PORTA PARA OS OBJETOS
- OBJETOS RECEBEM ADDR DO GATEWAY PARA REALIZAR CONEXÃO TCP POSTERIORMENTE

### receive_multicast_group.py
Recebimento de mensagem via multicast (função que é herdada pelo client.py).

Em client.py existe a função get_addr_by_mult(), que é responsável pelo recebimento do endereço do gateway (IP, PORT). Os objetos herdam a classe Client.

Logo, todos os objetos recebem uma mensagem contendo o IP e Porta do Gateway.

### send_multicast_group.py
Envio de mensagem via multicast (Função que é herdada pelo gateway.py)

No gateway.py a função send_gateway_address() realiza o envio da mensagem contendo seu IP e Porta. 

Logo, o gateway envia uma mensagem com seu IP e Porta para todos os clientes conectados ao multicast, ou seja, a todos os objetos. Mesmo que estes não estejam diretamente conectados ao gateway.

