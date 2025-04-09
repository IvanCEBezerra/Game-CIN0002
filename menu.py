import pygame

class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.largura, self.altura = self.tela.get_size()
        self.fonte_titulo = pygame.font.Font("m04b.ttf", 80)

        # Posicoes dos botoes (usadas para desenhar e para a mask)
        self.pos_jogar = (300, 200)
        self.pos_opcoes = (300, 300)
        self.pos_creditos = (300, 400)
        self.pos_sair = (300, 500)

        # Imagens
        self.img_jogar_default = pygame.image.load("imagens/menu/botões/default_jogar.png")
        self.img_jogar_hover = pygame.image.load("imagens/menu/botões/hover_jogar.png")

        self.img_opcoes_default = pygame.image.load("imagens/menu/botões/default_opções.png")
        self.img_opcoes_hover = pygame.image.load("imagens/menu/botões/hover_opções.png")

        self.img_creditos_default = pygame.image.load("imagens/menu/botões/default_créditos.png")
        self.img_creditos_hover = pygame.image.load("imagens/menu/botões/hover_créditos.png")

        self.img_sair_default = pygame.image.load("imagens/menu/botões/default_sair.png")
        self.img_sair_hover = pygame.image.load("imagens/menu/botões/hover_sair.png")

        # Masks para detecção pixel-perfect
        self.mask_jogar = pygame.mask.from_surface(self.img_jogar_default)
        self.mask_opcoes = pygame.mask.from_surface(self.img_opcoes_default)
        self.mask_creditos = pygame.mask.from_surface(self.img_creditos_default)
        self.mask_sair = pygame.mask.from_surface(self.img_sair_default)

    def desenhar_texto(self, texto, fonte, cor, x, y):
        render = fonte.render(texto, True, cor)
        rect = render.get_rect(center=(x, y))
        self.tela.blit(render, rect)

    def esta_sobre_pixel(self, mask, pos_img, mouse_pos):
        x, y = mouse_pos[0] - pos_img[0], mouse_pos[1] - pos_img[1]
        if 0 <= x < mask.get_size()[0] and 0 <= y < mask.get_size()[1]:
            return mask.get_at((x, y))
        return False

    def desenhar_botao_imagem(self, img_default, img_hover, pos_img, mouse_pos, mask):
        if self.esta_sobre_pixel(mask, pos_img, mouse_pos):
            self.tela.blit(img_hover, pos_img)
        else:
            self.tela.blit(img_default, pos_img)
    
    def tela_opcoes(self):
        executando = True
        volume = pygame.mixer.music.get_volume()  # Obtém o volume atual
        fonte_opcoes = pygame.font.Font("m04b.ttf", 35)  # Reduz o tamanho da fonte
        img_fundo_opcoes = pygame.image.load("imagens/IMG-8533.png").convert()  # Carrega a imagem de fundo

        while executando:
            self.tela.blit(img_fundo_opcoes, (0, 0))  # Desenha a imagem de fundo
            self.desenhar_texto("Musica", fonte_opcoes, (255, 255, 255), self.largura // 2, 50)
            self.desenhar_texto(f"Volume: {int(volume * 100)}%", fonte_opcoes, (255, 255, 255), self.largura // 2, 150)
            self.desenhar_texto("Pressione ESC para voltar", fonte_opcoes, (255, 255, 255), self.largura // 2, 250)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:  # Voltar ao menu principal
                        executando = False
                    elif evento.key == pygame.K_UP:  # Aumentar volume
                        volume = min(1.0, volume + 0.1)
                        pygame.mixer.music.set_volume(volume)
                    elif evento.key == pygame.K_DOWN:  # Diminuir volume
                        volume = max(0.0, volume - 0.1)
                        pygame.mixer.music.set_volume(volume)

            pygame.display.flip()

    def rodar(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Musicas/menu_song.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        executando = True
        self.img_fundo = pygame.image.load("imagens/IMG-8525.png").convert()
        while executando:
            self.tela.blit(self.img_fundo, (0, 0))
            mouse_pos = pygame.mouse.get_pos()

            self.desenhar_texto("CIn Flight", self.fonte_titulo, (255, 255, 255), self.largura // 2, 100)

            self.desenhar_botao_imagem(self.img_jogar_default, self.img_jogar_hover, self.pos_jogar, mouse_pos, self.mask_jogar)
            self.desenhar_botao_imagem(self.img_opcoes_default, self.img_opcoes_hover, self.pos_opcoes, mouse_pos, self.mask_opcoes)
            self.desenhar_botao_imagem(self.img_creditos_default, self.img_creditos_hover, self.pos_creditos, mouse_pos, self.mask_creditos)
            self.desenhar_botao_imagem(self.img_sair_default, self.img_sair_hover, self.pos_sair, mouse_pos, self.mask_sair)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.stop()
                    if self.esta_sobre_pixel(self.mask_jogar, self.pos_jogar, mouse_pos):
                        return "jogar"
                    if self.esta_sobre_pixel(self.mask_opcoes, self.pos_opcoes, mouse_pos):
                        self.tela_opcoes()
                    if self.esta_sobre_pixel(self.mask_sair, self.pos_sair, mouse_pos):
                        pygame.quit()
                        exit()
                    # Os outros botões ainda não têm funcionalidade

            pygame.display.flip()
