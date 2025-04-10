import pygame
import random
import constantes
from Hitabox import hitbox as hitbox

class GerenciadorColecionaveis:
  def __init__(self, escudo):
    self.coletavel = hitbox(constantes.X/2, constantes.Y/3, 'Imagens/coletáveis/pubomba.png')
    self.grupo_coletavel = pygame.sprite.Group()
    self.grupo_rodape_tiro = pygame.sprite.Group()
    self.grupo_rodape_escudo = pygame.sprite.Group()
    self.grupo_coletavel.add(self.coletavel)  # Adiciona o coletável ao grupo de coletáveis
    self.escudo = escudo
    self.coletavel.ativacao = False
    self.rodape = False
    self.countdown_tiros = 0
    self.countdown_escudo = 0
    self.tiro_rodape = hitbox(40, constantes.Y-40, 'Imagens/coletáveis/pubomba.png', id = constantes.TIRO_BOMBA)
    self.tiro_rodape.ativacao = False
    self.escudo_rodape = hitbox(110, constantes.Y-40, 'Imagens/coletáveis/puescudo.png', id = constantes.ESCUDO_ON)
    self.escudo_rodape.ativacao = False
    #print(100000000, constantes.FPS * constantes.INTERVALO_COLETAVEIS)

  def update(self, aviaozinho):
      col_id = None
      tipo_tiro = ""

      if not self.coletavel.ativacao:
          #fazer os coletáveis aparecerem aproximadamente de 10 em 10 segundos
          if random.randint(0, int(constantes.FPS * constantes.INTERVALO_COLETAVEIS)) == 0:
              self.coletavel.kill()

              #gerar aleatóriamente qual será o coletável
              col_aleatorio = random.randint(1, 5)
              #gerar uma posição aleatória para o coletável aparecer na tela
              pos_x_aleatorio = random.randint(20, 1250)

              if col_aleatorio == constantes.TIRO_BOMBA:
                  self.coletavel = hitbox(pos_x_aleatorio, 0, 'Imagens/coletáveis/pubomba.png', id = constantes.TIRO_BOMBA)
              elif col_aleatorio == constantes.ESCUDO_ON:
                  self.coletavel = hitbox(pos_x_aleatorio, 0, 'Imagens/coletáveis/puescudo.png', id = constantes.ESCUDO_ON)
              elif col_aleatorio == constantes.TIRO_TRIPLO:
                  self.coletavel = hitbox(pos_x_aleatorio, 0, 'Imagens/coletáveis/putiro3.png', id = constantes.TIRO_TRIPLO)
              elif col_aleatorio == constantes.TIRO_LIL:
                  self.coletavel = hitbox(pos_x_aleatorio, 0, 'Imagens/coletáveis/aviao_suporte.png', id = constantes.TIRO_LIL)

              self.grupo_coletavel.add(self.coletavel)  # Adiciona o coletável ao grupo de coletáveis
              self.coletavel.ativacao = True
              print('coletavel entrou na tela')

      if self.coletavel.ativacao:
          self.coletavel.mover_vertical(6)
          
          if aviaozinho.rect.colliderect(self.coletavel.rect):
              self.coletavel.kill()
              self.coletavel.ativacao = False
              print('pegou coletavel')

              if self.coletavel.id == constantes.TIRO_BOMBA:
                  self.countdown_tiros = constantes.DURACAO_TIRO * constantes.FPS
                  # tipo_tiro = "Bomb"
                  col_id = constantes.TIRO_BOMBA
                  self.tiro_rodape = hitbox(40, constantes.Y-40, 'Imagens/coletáveis/pubomba.png', id = constantes.TIRO_BOMBA)
                  self.grupo_rodape_tiro.add(self.tiro_rodape)

              elif self.coletavel.id == constantes.ESCUDO_ON:
                  self.countdown_escudo = constantes.DURACAO_ESCUDO * constantes.FPS
                  # self.escudo.ativacao = True
                  col_id = constantes.ESCUDO_ON
                  self.escudo_rodape = hitbox(110, constantes.Y-40, 'Imagens/coletáveis/puescudo.png', id = constantes.ESCUDO_ON)
                  self.grupo_rodape_escudo.add(self.escudo_rodape)

              elif self.coletavel.id == constantes.TIRO_TRIPLO:
                  self.countdown_tiros = constantes.DURACAO_TIRO * constantes.FPS
                  # tipo_tiro = "Triplo"
                  col_id = constantes.TIRO_TRIPLO
                  self.tiro_rodape = hitbox(40, constantes.Y-40, 'Imagens/coletáveis/putiro3.png', id = constantes.TIRO_TRIPLO)
                  self.grupo_rodape_tiro.add(self.tiro_rodape)

              elif self.coletavel.id == constantes.TIRO_LIL:
                  self.countdown_tiros = constantes.DURACAO_TIRO * constantes.FPS
                  # tipo_tiro = "Follower"
                  col_id = constantes.TIRO_LIL
                  self.tiro_rodape = hitbox(40, constantes.Y-40, 'Imagens/coletáveis/aviao_suporte.png', id = constantes.TIRO_LIL)
                  self.grupo_rodape_tiro.add(self.tiro_rodape)

              self.rodape = True

              print('pegou coletavel', self.coletavel.id)

          if self.coletavel.rect.top > constantes.Y:
              self.coletavel.kill()
              self.coletavel.ativacao = False
              self.coletavel.id = constantes.TIRO_DEFAULT
              print('perdeu coletavel')

      if self.countdown_tiros > 0:
          if aviaozinho.rect.colliderect(self.coletavel.rect) and self.coletavel.id != 2:
              duracao_tiro = constantes.DURACAO_TIRO
 
          else:
              self.countdown_tiros -= 1
              #print(self.countdown_tiros)
              if self.countdown_tiros == 0:
                  #tipo_tiro = "Default"
                  col_id = constantes.TIRO_DEFAULT
                  self.tiro_rodape.kill()
                  for t in self.grupo_rodape_tiro:
                    if t != self.escudo_rodape:
                        self.grupo_rodape_tiro.remove(t)
                  self.rodape = False
                  #print(self.grupo_rodape_tiro)
                  print('tiro powerup acabou')

      if self.countdown_escudo > 0:
          if aviaozinho.rect.colliderect(self.coletavel.rect) and self.coletavel.id == 2:
              duracao_escudo = constantes.DURACAO_ESCUDO

          else:
              self.countdown_escudo -= 1
              #print(self.countdown_escudo)
              if self.countdown_escudo == 0:
                  self.escudo.ativacao = False
                  col_id = constantes.ESCUDO_OFF
                  self.escudo_rodape.kill()
                  for i in self.grupo_rodape_escudo:
                    if i == self.escudo_rodape:
                        self.grupo_rodape_escudo.remove(i)
                  self.rodape = False
                  #print(self.grupo_rodape_escudo)
                  print('escudo acabou')

      return col_id