Relatório do Cin Flight
Participantes: 
Titho Lívio Duarte Melo <tldm>
Ivan Carvalho Ernesto Bezerra <iceb>
Maria Luisa de Alcântara Sodré  <mlas4>
Maria Clara Rodrigues de Almeida <mcra2>
Edivaldo Ambrósio da Silva Filho <easf>
Guilherme de Carvalho Fabri <gcf2>
Gustavo Cravo Teixeira Filho <gctf>
Edivaldo Ambrósio da Silva Filho <easf>

Arquitetura.
  O código foi arquitetado em ser feito por classes separadas em arquivos diferentes de cada grupo de objetos exceto o dos inimigos que foi feito em duas classes no mesmo arquivo sendo nomeados de : (Hitbox,GerenciadorColetaveis,menu,inimigo_horizontal, kamikaze).
  A classe Hitbox foi a base para o código do avião(player) e das duas classes de inimigos e dos coletáveis ela definia um retângulo de eixos x e y como área de contato com base na imagem colocada para cada objeto. 
  A classe GerenciadorColetaveis aproveitava a classe hitbox para criar as funções da interação de cada coletável com o player, além de avisar quando o coletável era coletado com um ícone no canto inferior esquerdo da tela. 
  A classe menu serve para a geração do menu inicial do jogo definindo os botões, as fontes das letras e as medidas da tela inicial. 
  As duas classes dos inimigos foram feitas em partes separadas por conta dos dois objetos se comportarem de maneiras diferentes e independentes com o inimigo_horizontal sendo um objeto que surge no topo da tela e vai descendo se movendo para a esquerda e para a direita enquanto desce disparando balas que se entrarem em contato com o avião ele tira 1 vida, já o “kamikaze” faz referência a um tipo de aeronave japonesa da segunda guerra mundial que possui como único intuito se jogar contra os seus adversários morrendo ambos os pilotos dessa forma foi criada essa classe que só se movimenta para baixo não dispara e quando encostado com o player tira uma vida.
  O fps, cooldown para cada habilidade e os valores dos eixo x e y foram salvos como variáveis dentro de um arquivo chamado constantes em prol da organização do projeto. co
  Depois o sistema de vida, a movimentação do player, os disparos do player e dos inimigos, a tela de game over, o respawn do inimigo, a aparição e colisão dos coletáveis e a música os efeitos sonoros foram adicionados e definidos no código main com partes dentro do while e fora do while que só acaba quando o jogo é fechado.
  

Ferramentas, Bibliotecas e Framework.
  As principais ferramentas que utilizamos foram o Visual Studio Code e Pycharm para codificar os códigos indo de preferência a cada membro, porém pelo fato de já estar instalado é mais fácil de começar sempre que utilizamos o pycharm foi no laboratório.
  A biblioteca que utilizamos foi o pygame e a random, por conta do pygame ser uma das melhores bibliotecas para o desenvolvimento de jogos por conta de ser uma biblioteca focada em orientação a objeto nós utilizamos ela para montar maior parte do código. Entretanto o pygame não resolvia tudo então entra na jogada o random ele foi necessário para o spawn dos inimigos e dos power ups pegando uma posição aleatória dentro do eixo x da tela para depois descer do y/20 até o final do eixo y.
  O framework que foi utilizado foi o bizagi para coordenar os projetos por etapas separadas por etapas e por uma ordem de onde começar e onde terminar para organizar e coordenar a equipe, além de separar cada etapa com cada código dentro dos branches do github.
Divisão do Trabalho.
  Durante o carnaval os membros Thito e Ivan acabaram adiantando boa parte do projeto fazendo as suas parte antes de todos, dessa forma o resto do grupo pegou as partes que faltavam para finalizar o projeto que serão detalhadas a seguir seguindo a ordem de finalização.

Ivan Carvalho Ernesto Bezerra <iceb> Ivan fez o background da tela, a movimentação do avião principal (player), a trilha sonora junto dos sound effects junto da Maria Clara, e o gerenciamento do código.

Titho Lívio Duarte Melo <tldm> : Titho criou a classe hitbox, que servia para criar uma hitbox para os futuros objetos e para o avião,fez todos os tipos de projéteis e o escudo.

Maria Luisa de Alcântara Sodré  <mlas4>:Maria Luisa desenvolveu a classe dos coletáveis e aplicou todos os tipos de projéteis e o escudo quando coletado pelo player

Maria Clara Rodrigues de Almeida <mcra2>:Maria Clara criou o design de tudo dentro do jogo e fez o sistema do menu do jogo junto de Ivan.

Guilherme de Carvalho Fabri <gcf2>: Fabri trabalhou nas classes dos inimigos e no sistema de vida e na tela de game over junto do Gustavo Edivaldo e Thito.

Gustavo Cravo Teixeira Filho <gctf>: Gustavo trabalhou no surgimento dos inimigos e no primeiro sistema de morte junto do Fabri e Edivaldo

Edivaldo Ambrósio da Silva Filho <easf>: Edivaldo trabalhou na tela de game over, os tiros dos inimigos, e auxiliou na produção da apresentação. 


Conceitos.

  Os conceitos aprendidos durante a disciplina que foram utilizados no projeto foram as: Listas já que os grupos do pygame são bem semelhantes às listas do python e utilizamos para cada grupo do jogo(avião, coletáveis e inimigos). Booleanas  que foram utilizadas para ativação dos (power up, spawn inimigo, spawn avião,manter o jogo rodando). Funções para a movimentação do avião(player). Laço para manter o jogo rodando dentro de um while True que quando o jogo era fechado se tornava False assim encerrando o jogo. Dicionário para salvar as colisões dos grupos de inimigos com o grupo de projéteis.


Desafios e Erros.

  Quando começamos o projeto o maior desafio foi o estudo da biblioteca pygame e a programação orientada a objeto, por conta desse conteúdos não terem sido dados durante a disciplina de maneira mais direta nós tivemos uma grande dificuldade em iniciar o projeto.
Qual foi o maior erro ?
  O maior erro do projeto foi a falta de um método definido de estudo com a biblioteca estávamos bastante perdidos no começo, porém com as indicações do Ivan e do Thito conseguimos criar um sistema de estudo que segue pelo esquema de assistir as video aulas do redu sobre programação orientada a objetos, uma vídeo aula detalhada em inglês e a leitura do site do pygame que explicava cada  da biblioteca.


Qual foi o maior desafio ?

  Quando começamos o projeto o maior desafio foi o estudo da biblioteca pygame e a programação orientada a objeto, por conta desse conteúdos não terem sido dados durante a disciplina de maneira mais direta nós tivemos uma grande dificuldade em iniciar o projeto, além de aprender a mexer no github para conseguir atualizar um código em partes.


Quais lições aprendidas durante o projeto ?

  Como funciona programação orientada a objetos, como se organizar em um trabalho em grupo, como funciona a biblioteca pygame e random, como pesquisar e estudar bibliotecas e diferentes formas de programação.
