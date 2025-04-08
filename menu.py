import pygame

class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.largura, self.altura = self.tela.get_size()
        self.fonte_titulo = pygame.font.SysFont("Reydex", 60)
        self.fonte_botao = pygame.font.SysFont("Reydex", 36)

        self.botao_jogar = pygame.Rect(300, 250, 200, 50)
        self.botao_sair = pygame.Rect(300, 350, 200, 50)

    def desenhar_texto(self, texto, fonte, cor, x, y):
        render = fonte.render(texto, True, cor)
        rect = render.get_rect(center=(x, y))
        self.tela.blit(render, rect)

    def desenhar_botao(self, texto, rect, mouse_pos):
        if rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.tela, (0, 0, 0), rect)
        else:
            pygame.draw.rect(self.tela, (0, 120, 215), rect)
        
        texto_render = self.fonte_botao.render(texto, True, (255, 255, 255))
        texto_rect = texto_render.get_rect(center=rect.center)
        self.tela.blit(texto_render, texto_rect)

    def rodar(self):
        executando = True
        while executando:
            self.tela.fill((50, 50, 50))
            mouse_pos = pygame.mouse.get_pos()

            self.desenhar_texto("CIn Fligth", self.fonte_titulo, (255, 255, 255), self.largura // 2, 100)
            self.desenhar_botao("Jogar", self.botao_jogar, mouse_pos)
            self.desenhar_botao("Sair", self.botao_sair, mouse_pos)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.botao_jogar.collidepoint(mouse_pos):
                        return "jogar"
                    if self.botao_sair.collidepoint(mouse_pos):
                        pygame.quit()
                        exit()

            pygame.display.flip()
