# CInFlitgh
import pygame

pygame.init()
# dimensões da tela
x = 800
y = 500
tela = pygame.display.set_mode((x, y))
# nome no topo da tela
pygame.display.set_caption("CInFligth")
# importa contagem de tempo que o jogo está aberto
clock = pygame.time.Clock()
# variavel que via conferir se o jogo está aberto
rodando = True
# define que o player vai começar no centro da tela
player_pos = pygame.Vector2(x/2 , y/2)

'Arquivos de imagens do jogo'
fundo = pygame.image.load("enhanced_battlefield_map.jpg").convert()

'Variaveis do jogo'
velocidade = 50

while rodando:
    # mantém a velocidade de jogo indeoendente da taxa fps
    delta_time = clock.tick(120)/100

    'Processa os eventos do jogo'
    for evento in pygame.event.get():

        # se clicar no botão X na janela fecha
        if evento.type == pygame.QUIT:
            rodando = False
    
    # indica que o plano de fundo, deve estar no loop para que os aviões movimentados não se sobrepoam
    tela.blit(fundo, (0,0))

    # cria personagem: um retângulo prata
    pygame.draw.rect(tela, "silver", (player_pos.x, player_pos.y, 40, 60))

    'Controles - botões e comandos'
    # movimentos do player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_pos.y  -= velocidade * delta_time
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_pos.y  += velocidade * delta_time
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_pos.x  -= velocidade * delta_time
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] :
        player_pos.x  += velocidade * delta_time
    # evita que ele saia da tela
    player_pos.x = max(0, min(player_pos.x, x-40))
    player_pos.y = max(0, min(player_pos.y, y-60))

    # atualiza a display
    pygame.display.flip()

pygame.quit()

