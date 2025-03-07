# CInFlitgh
import pygame

pygame.init()
# dimensões da tela
x = 1280
y = 720
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
fundo_arquivo = pygame.image.load("Imagens/enhanced_battlefield_map.jpg").convert()
fundo = pygame.transform.smoothscale(fundo_arquivo, (x, y))
player_img_reto = pygame.image.load("Imagens/aviao_reto.png").convert_alpha()
player_img_esq = pygame.image.load("Imagens/aviao_esquerda.png").convert_alpha()
player_img_dir = pygame.image.load("Imagens/aviao_direita.png").convert_alpha()


'Variaveis do jogo'
velocidade = 130
velocidade_fundo = 50
offset_y = 0
fazendo_curva = False


while rodando:
    # mantém a velocidade de jogo indeoendente da taxa fps
    delta_time = clock.tick(120)/1000

    'Processa os eventos do jogo'
    for evento in pygame.event.get():

        # se clicar no botão X na janela fecha
        if evento.type == pygame.QUIT:
            rodando = False
    
    'Movimentação do fundo da tela'
    # define que a cada frame o fundo se move a velociade definida na vertical
    offset_y += velocidade_fundo * delta_time
    # se a imagem de fundo acbar ele reseta
    if offset_y > y:
        offset_y -= y
    # indica que o plano de fundo, deve estar no loop para que os aviões movimentados não se sobrepoam
    tela.blit(fundo, (0,offset_y))
    # faz com que o loop pareça continuo
    tela.blit(fundo, (0,offset_y-y))


    'Controles - botões e comandos'
    # movimentos do player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_pos.y  -= velocidade * delta_time
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_pos.y  += velocidade * delta_time
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_pos.x  -= velocidade * delta_time
        fazendo_curva = True
        tela.blit(player_img_esq, (player_pos.x, player_pos.y))
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] :
        player_pos.x  += velocidade * delta_time
        tela.blit(player_img_dir, (player_pos.x, player_pos.y))
        fazendo_curva = True
    
    #caracteriza o aviao quando ele não está indo pros lados
    if not fazendo_curva:
        tela.blit(player_img_reto, (player_pos.x, player_pos.y))
    fazendo_curva = False
    
    # evita que ele saia da tela
    player_pos.x = max(0, min(player_pos.x, x-40))
    player_pos.y = max(0, min(player_pos.y, y-60))

    # atualiza a display
    pygame.display.flip()

pygame.quit()

