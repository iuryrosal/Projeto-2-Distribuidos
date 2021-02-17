# Sistemas Distribuidos
 Aqui estão reunidos os projetos realizados dentro da disciplina de Sistemas Distribuídos do curso de Engenharia de Computação (Universidade Federal do Ceará - UFC). Os projetos foram feitos via linguagem Python. Esses projetos foram realizados pelo time composto por:
 - Iury Lima Rosal
 - Luís Gustavo de Castro
 - Vinicius Almeida de Castro
 
Projetos:
- Calculadora_UDP: consiste em, utilizando UDP, implementar uma calculadora remota que execute as 4 operações básicas (+, -, x, /) de números decimais. Descreva o formato para cada tipo das mensagens (Request e Response).

- Chat_TCP: consiste em implementar um Chat usando TCP. O Chat deve suportar múltiplos clientes e um servidor. Todos os clientes devem estar na mesma sala do chat (as mensagens enviadas por um cliente devem ser recebidas por todos os clientes). Comandos que o usuário (cliente) pode enviar: 
  - /ENTRAR: ao usar esse comando, ele é requisitado a digitar IP, porta do servidor e nickname que deseja usar no chat (não precisa tratar nicknames repetidos);
  - Uma vez conectado, o cliente pode enviar mensagens para a sala do chat;
  - /USUARIOS: ao enviar esse comando, o cliente recebe a lista de usuários atualmente conectados ao chat; 
  - /SAIR: ao enviar esse comando, uma mensagem é enviada à sala do chat informando que o usuário está saindo e encerra a participação no chat.

- Ambiente Inteligente:
  - Uma aplicação (móvel, desktop ou web) deve ser implementada para permitir ao usuário conectar e visualizar o status dos objetos do ambiente inteligente, além de atuar e ler os dados dados dos objetos.
  - A aplicação deve se conectar a um servidor, chamado de Gateway, que se comunica com cada um dos objetos "inteligentes" do local. A comunicação entre aplicação e o Gateway deve ser implementada utilizando TCP e as mensagens definidas com Protocol Buffers.
  - Deve haver, pelo menos, dois tipos de mensagens (Request e Response) cujos formatos devem ser definidos pelo grupo.
  - O ambiente inteligente deve conter, no mínimo, 3 equipamentos (lâmpadas, tv, ar condicionado, etc...).
  - A comunicação do Gateway com os equipamentos fica a critério do time. Tais equipamentos podem ser todos simulados por software, que envia de forma periodica seu estatus (ou quando ele se modifica) e recebe comandos para ligar/desligar ou realizar alguma operação.
  - O Gateway deve ter uma funcionalidade de descobertas de equipamentos inteligentes, usando comunicação em grupo. Ao iniciar o Gateway, ele deve enviar uma mensagem solicitando que os equipamentos se identifiquem. 
  - Ao iniciar o processo dos equipamentos inteligentes, estes devem enviar mensagem se identificando para o Gateway. A identificação significa enviar seu tipo (lâmpada, ar condicionado, etc..), Ip e Porta para o Gateway.
  - Pelo menos um dos equipamentos deve atuar como um sensor contínuo, que envia a cada ciclo de X segundos um valor para o Gateway (um sensor de temperatura).
  - Pelo menos um dos equipamentos deve ter comportamento de um atuador (recebe comandos para atualizar seu status, como ligar/desligar).
