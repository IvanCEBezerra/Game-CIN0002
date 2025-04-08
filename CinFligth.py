
# CInFlight
import pygame
import constantes
from Hitabox import hitbox as hitbox
from GerenciadorColecionaveis import GerenciadorColecionaveis as gc
from menu import Menu

# Inicializa o pygame
pygame.init()

# Define o valor do score e a fonte de texto do score (seu tipo e seu tamanho)
fonte_score = pygame.font.SysFont("comicsanss", 40)
score = 0

# Dimensões da tela
x = 1280  # Largura da tela
y = 720   # Altura da tela

# Definição das proporções da tela (janela onde vai ocorrer o jogo)
tela = pygame.display.set_mode((x, y), pygame.FULLSCREEN)

menu = Menu(tela)
opcao = menu.rodar()
if opcao != "jogar":
    pygame.quit()
    exit()

# Define o background do jogo, utilizando uma imagem externa
fundo = pygame.image.load("Imagens/background.png")

# Taxa de scroll do fundo
fundo_scroll = -y

# Texto que vai aparecer na parte superior da tela
pygame.display.set_caption("CInFligth")

# Cria um relógio que permite controlar a taxa de atualização da tela e a execução do loop de jogo
clock = pygame.time.Clock()

# Define a taxa máxima de quadros por segundo
fps = 30
# define velociade do avião
velocidade_aviao = 8

# Criação do primeiro hitbox do player do jogo (o aviaozinho), e o coloca em um grupo de sprites (para ser renderizado dentro do loop do jogo)
aviaozinho = hitbox(x / 2, y / 1.3, 'Imagens/avião_principal_neutro.png')
aviaozinho.ativacao = False  # Define se o aviaozinho está ativado
grupo_aviaozinho = pygame.sprite.Group()  # Cria o grupo de sprites para o aviaozinho
grupo_aviaozinho.add(aviaozinho)

grupo_lil_aviao = pygame.sprite.Group()  # Cria o grupo de sprites para os pequenos aviões (se necessário)

# Define os grupos e listas que vão manter os hitboxes das balas
grupo_tiro = pygame.sprite.Group()  # Grupo de tiros (balas)
lista_tiro_triplo = []  # Lista de tiros do tipo "triplo"
grupo_bomba = pygame.sprite.Group()  # Grupo de bombas

#Define o escudo, e o grupo do escudo.
escudo = hitbox(aviaozinho.rect.center[0], aviaozinho.rect.center[1], 'Imagens/shield.png')
grupo_escudo = pygame.sprite.Group()
escudo.ativacao = False

# Define o tipo de tiro (default por base) // Para os powerups
tipo_tiro = "Default"

# Cooldown do tiro (intervalo entre os tiros)
cooldown = fps/3

gerenciador_coletaveis = gc(escudo)

# Variável que verifica se o jogo está aberto
rodando = True

# Loop do jogo
while rodando:
    # Limita o número de quadros que o jogo pode renderizar por segundo, garantindo que o FPS não ultrapasse o valor definido
    clock.tick(fps)

    # Processa os eventos do jogo
    for evento in pygame.event.get():
        # Se clicar no botão X na janela, o jogo é fechado
        if evento.type == pygame.QUIT:
            rodando = False
    
    # Verifica as teclas pressionadas
    tecla = pygame.key.get_pressed()

    # Se a tecla para cima (↑) estiver pressionada e o avião não estiver fora da tela (com base na posição y do topo do hitbox)
    if (tecla[pygame.K_UP] == True or tecla[pygame.K_w] == True) and aviaozinho.rect.top > 0:
        aviaozinho.mover_vertical(-velocidade_aviao)
    
    # Se a tecla para baixo (↓) estiver pressionada e o avião não estiver fora da tela (com base na posição y do fundo do hitbox)
    if (tecla[pygame.K_DOWN] == True or tecla[pygame.K_s] == True) and aviaozinho.rect.bottom < y:
        aviaozinho.mover_vertical(velocidade_aviao)
    
    # Se a tecla para direita (→) estiver pressionada e o avião não ultrapassar o limite da tela (com base na posição x da parte direita do hitbox)
    if (tecla[pygame.K_RIGHT] == True or tecla[pygame.K_d] == True) and aviaozinho.rect.right < x:
        aviaozinho.mover_horizontal(velocidade_aviao)

        # Altera a imagem para a direita
        aviaozinho.image = pygame.image.load("Imagens/aviao_principal_direita.png")  
    
    # Se a tecla para esquerda (←) estiver pressionada e o avião não ultrapassar o limite da tela (com base na posição x da parte esquerda do hitbox)
    if (tecla[pygame.K_LEFT] == True or tecla[pygame.K_a] == True) and aviaozinho.rect.left > 0:
        aviaozinho.mover_horizontal(-velocidade_aviao)

        # Altera a imagem para a esquerda
        aviaozinho.image = pygame.image.load("Imagens/aviao_principal_esquerda.png")

    # Se o escudo estiver ativado ou estiver nulo, atualize a posição dele
    if escudo.ativacao == True or escudo.ativacao == None:
        escudo.rect.center = aviaozinho.rect.center
    # Caso o escudo foi destruido, delete escudo, crie um novo, e deixe-o no modo neutro
    elif escudo.ativacao == False:
        escudo.kill()
        escudo = hitbox(aviaozinho.rect.center[0], aviaozinho.rect.center[1], 'Imagens/shield.png')
        grupo_escudo.add(escudo)
        escudo.ativacao = None
    
    # Lógica de ativação do avião pequeno quando o tipo de tiro "Follower" é selecionado
    if aviaozinho.ativacao == True and tipo_tiro != "Follower":
        lil_aviao.kill()  # Mata o pequeno avião se o tipo de tiro não for "Follower"
        aviaozinho.ativacao = False  # Desativa o aviaozinho
    elif aviaozinho.ativacao == True:
        # Mover o pequeno avião em direção ao aviaozinho
        if lil_aviao.rect.left <= aviaozinho.rect.left - 48:
            lil_aviao.mover_horizontal(velocidade_aviao)
        if lil_aviao.rect.right >= aviaozinho.rect.right + 48:
            lil_aviao.mover_horizontal(-velocidade_aviao)
        if lil_aviao.rect.top <= aviaozinho.rect.top - 48:
            lil_aviao.mover_vertical(velocidade_aviao)
        if lil_aviao.rect.bottom >= aviaozinho.rect.bottom + 48:
            lil_aviao.mover_vertical(-velocidade_aviao)
    elif tipo_tiro == "Follower" and aviaozinho.ativacao == False:
        aviaozinho.ativacao = True  # Ativa o aviaozinho
        lil_aviao = hitbox(aviaozinho.rect.left + 44, aviaozinho.rect.bottom + 25,"Imagens/av_suporte_neutro.png" )
        grupo_lil_aviao.add(lil_aviao)  # Adiciona o pequeno avião ao grupo

    # Se a tecla espaço estiver pressionada, o cooldown for um terço do valor do fps, e o tipo de tiro for default, crie a hitbox de um tiro e o coloque no grupo de tiros, e resete o cooldown
    if tecla[pygame.K_SPACE] == True and cooldown >= fps/1.9 and (tipo_tiro == "Default" or tipo_tiro == "Follower"):
        tiro = hitbox(aviaozinho.rect.midtop[0], aviaozinho.rect.midtop[1], "Imagens/bullet.png")
        grupo_tiro.add(tiro)
        if tipo_tiro == "Follower":
            # Se o tipo de tiro for "Follower", cria tiros para o pequeno avião também
            lil_tiro = hitbox(lil_aviao.rect.midtop[0], lil_aviao.rect.midtop[1], "Imagens/bullet.png")
            grupo_tiro.add(lil_tiro)
        cooldown = 1  # Reseta o cooldown após atirar
    
    # Se a tecla do espaço estiver pressionada, o cooldown for um terço do valor do fps, e o tipo do tiro for default, crie três linhas de tiros diferentes, e os guarde junto com a posição do meio do aviaozinho após a criação das balas (E resete o cooldown)
    elif tecla[pygame.K_SPACE] == True and cooldown >= fps and tipo_tiro == "Triplo":
        tiros = pygame.sprite.Group()  # Cria um novo grupo para os tiros
        tiro_middle = hitbox(aviaozinho.rect.midtop[0], aviaozinho.rect.midtop[1], "Imagens/bullet.png")
        tiro_middle.posicao_spawn = aviaozinho.rect.midtop[0]  # Define a posição de spawn do tiro do meio
        tiro_left = hitbox(aviaozinho.rect.topleft[0], aviaozinho.rect.topleft[1], "Imagens/bullet.png")
        tiro_left.posicao_spawn = aviaozinho.rect.midtop[0]  # Define a posição de spawn do tiro esquerdo
        tiro_right = hitbox(aviaozinho.rect.topright[0], aviaozinho.rect.topright[1], "Imagens/bullet.png")
        tiro_right.posicao_spawn = aviaozinho.rect.midtop[0]  # Define a posição de spawn do tiro direito
        tiros.add(tiro_left)
        tiros.add(tiro_middle)
        tiros.add(tiro_right)
        lista_tiro_triplo.append(tiros)  # Adiciona o grupo de tiros à lista de tiros triplos

        cooldown = 1  # Reseta o cooldown após atirar
    
    elif tecla[pygame.K_SPACE] == True and cooldown >= fps * 1.2 and tipo_tiro == "Bomb":
        bomb = hitbox(aviaozinho.rect.midtop[0], aviaozinho.rect.midtop[1], "Imagens/bomb.png")
        bomb.ativacao = False  # A bomba começa desativada
        bomb.posicao_spawn = aviaozinho.rect.midtop[1]  # Define a posição de spawn da bomba
        grupo_bomba.add(bomb)  # Adiciona a bomba ao grupo de bombas
        cooldown = 1  # Reseta o cooldown após lançar a bomba

    # Se nenhuma das teclas esquerda ou direita estiver pressionada, a imagem do avião volta para a posição inicial
    if (tecla[pygame.K_LEFT] == False and tecla[pygame.K_a] == False) and (tecla[pygame.K_RIGHT] == False and tecla[pygame.K_d] == False):
        aviaozinho.image = pygame.image.load("Imagens/avião_principal_neutro.png")

    coletavel_id = gerenciador_coletaveis.update(aviaozinho)

    # Se o coletável for ativado, e o id do coletável for diferente de 0, faça a lógica de ativação do coletável
    if coletavel_id != None:
        if coletavel_id == constantes.TIRO_DEFAULT:
            tipo_tiro = "Default"
        elif coletavel_id == constantes.TIRO_BOMBA:
            tipo_tiro = "Bomb"
        elif coletavel_id == constantes.ESCUDO_ON:
            escudo.ativacao = True
        elif coletavel_id == constantes.ESCUDO_OFF:
            escudo.ativacao = False
        elif coletavel_id == constantes.TIRO_TRIPLO:
            tipo_tiro = "Triplo"
        elif coletavel_id == constantes.TIRO_LIL:
            tipo_tiro = "Follower"

    # Invoca e focaliza o fundo no centro da tela, desenhando o plano de fundo
    tela.blit(fundo, (0, fundo_scroll))

    # O fundo se move para cima de três em três pixels
    fundo_scroll += 7

    # Caso o fundo chegue no último pixel superior (y), resete para a posição de fundo inicial
    if fundo_scroll > 0:
        fundo_scroll = -y

    # Para cada bala atirada, se a bala tocar no limite superior da tela, remova a bala do grupo
    if len(grupo_tiro) > 0:
        for bala in grupo_tiro:
            if bala.rect.y > 0:
                bala.rect.y -= 25
            else:
                bala.kill()

    # Para cada linha de tiro, se a bala estiver em uma das extremidades, vá para um pouco para a diagonal e siga reto depois. Caso não seja, apenas siga reto.
    if len(lista_tiro_triplo) > 0:
        for linha in lista_tiro_triplo:
            i = 0
            for bala in linha:
                if i == 0:
                    if bala.rect.y > 0 and bala.rect.x > bala.posicao_spawn - 92:
                        bala.rect.y -= 4 * 1.414
                        bala.rect.x -= 4 * 1.414
                    elif bala.rect.y > 0:
                        bala.rect.y -= 20
                    else:
                        bala.kill()
                elif i == 1:
                    if bala.rect.y > 0:
                        bala.rect.y -= 20
                    else:
                        bala.kill()
                elif i == 2:
                    if bala.rect.y > 0 and bala.rect.x < bala.posicao_spawn + 70:
                        bala.rect.y -= 4 * 1.414
                        bala.rect.x += 4 * 1.414
                    elif bala.rect.y > 0:
                        bala.rect.y -= 20

                    else:
                        bala.kill()
                i += 1
    
    if len(grupo_bomba) > 0:
        for bomba in grupo_bomba:
            if bomba.rect.y > bomba.posicao_spawn - 290 and bomba.rect.y > 0:
                bomba.rect.y -= velocidade_aviao
            else:
                bomba.ativacao = True
                tempx = bomba.rect.x
                tempy = bomba.rect.y
            
            if bomba.ativacao == True and bomba.tempo_existencia == 0:
                bomba.image = pygame.image.load("Imagens/explosion.png")
                bomba.rect = bomba.image.get_rect()
                bomba.rect.center = [tempx, tempy]
            
            if bomba.ativacao == True and bomba.tempo_existencia < 10:
                bomba.tempo_existencia +=1
            elif bomba.ativacao == True:
                bomba.kill()
    
    # Define o texto do score a ser exibido na tela (e a sua cor)
    texto = fonte_score.render("Score: " + str(score), True, (0, 0, 0))

    # Demonstra o score to player
    tela.blit(texto, [0, 0])

    # Desenha todos os sprites dentro de cada grupo
    grupo_aviaozinho.draw(tela)
    if escudo.ativacao == True:
        grupo_escudo.draw(tela)
    if aviaozinho.ativacao == True:
        grupo_lil_aviao.draw(tela)
    grupo_tiro.draw(tela)
    grupo_bomba.draw(tela)
    for linha in lista_tiro_triplo:
        linha.draw(tela)
    if gerenciador_coletaveis.coletavel.ativacao == True:
        gerenciador_coletaveis.grupo_coletavel.draw(tela)
    #if gerenciador_coletaveis.rodape == True:
    if len(gerenciador_coletaveis.grupo_rodape_tiro) > 0:
        gerenciador_coletaveis.grupo_rodape_tiro.draw(tela)
    if len(gerenciador_coletaveis.grupo_rodape_escudo) > 0:
        gerenciador_coletaveis.grupo_rodape_escudo.draw(tela)

    # Atualiza a tela a cada iteração do loop
    pygame.display.update()

    # Aumente o cooldown em um 
    cooldown += 1

# Fecha o pygame quando o loop terminar
pygame.quit()
