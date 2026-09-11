O projeto Yumi_Roux | Meta City RP foi desenvolvido em Python utilizando o framework Flet, com o objetivo de criar uma
aplicação gráfica interativa inspirada no universo de FiveM Roleplay e na personagem Yumi_Roux. A proposta foi desenvolver
um painel que simulasse o ambiente de uma streamer dentro de Meta City, permitindo visualizar e controlar diferentes 
informações da personagem de maneira dinâmica.

A aplicação possui um Dashboard principal que apresenta informações como quantidade de espectadores, saldo, reputação,
nível, localização, veículo atual, combustível, missão e rádio. Os dados são atualizados conforme o usuário interage com
os recursos disponíveis no sistema, tornando a aplicação mais dinâmica e próxima de um painel de controle de personagem.

Também foi desenvolvido um sistema de personagem que permite acompanhar o nível e a experiência da Yumi_Roux. Através das 
interações disponíveis, é possível ganhar XP, aumentar a reputação e evoluir de nível. Quando a experiência necessária é 
atingida, o sistema realiza automaticamente o Level Up da personagem.

A aplicação também conta com uma garagem interativa onde é possível visualizar diferentes veículos, selecionar qual veículo 
utilizar, abastecer e dirigir pela cidade. Cada veículo possui seu próprio nível de combustível e o sistema controla a 
quantidade disponível durante as viagens. Foi adicionada uma validação para impedir que o combustível fique com valores 
negativos ou ultrapasse 100%, evitando erros na barra de progresso e mantendo o funcionamento correto da aplicação quando
o combustível chega a zero.

O sistema de missões permite aceitar e concluir diferentes atividades dentro de Meta City. Cada missão possui uma 
recompensa em dinheiro e uma quantidade de XP. Ao concluir uma missão, o saldo, a experiência e a reputação da personagem 
são atualizados automaticamente, permitindo que o jogador evolua através das atividades realizadas.

Também foi criado um inventário para controlar os itens da personagem, como celular, kit médico, rádio e dinheiro. 
Os itens podem ser utilizados e suas quantidades são atualizadas de acordo com as ações realizadas pelo usuário. 
Além disso, é possível adicionar determinados itens ao inventário através dos botões disponíveis na interface.

Outro recurso desenvolvido foi a Meta City Radio, que permite controlar uma rádio fictícia dentro da aplicação. 
O usuário pode reproduzir ou pausar a rádio, avançar ou voltar músicas e controlar o volume. As informações da música 
atual e do estado da rádio são atualizadas de forma dinâmica.

A aplicação possui ainda um chat lateral que simula os comentários de uma transmissão ao vivo. O usuário pode visualizar 
mensagens fictícias dos espectadores e enviar suas próprias mensagens, que são adicionadas automaticamente ao chat.

Durante o desenvolvimento foram utilizados conceitos importantes da linguagem Python, como variáveis, funções, listas, 
dicionários, estruturas condicionais, laços de repetição, funções lambda, eventos, manipulação de estados, atualização
dinâmica de componentes e geração de valores aleatórios através da biblioteca random. O Flet foi utilizado para construir
toda a interface gráfica e permitir que as ações realizadas pelo usuário modificassem os dados apresentados na tela.

Para executar o projeto é necessário ter o Python instalado e instalar o Flet através do comando pip install flet. 
Depois disso, o programa pode ser iniciado utilizando o comando python main.py. O projeto foi desenvolvido com foco
em praticar programação em Python e desenvolvimento de interfaces gráficas, transformando uma ideia relacionada a FiveM 
e Roleplay em uma aplicação interativa e funcional.
