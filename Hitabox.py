import pygame

# Define uma nova classe hitbox com as mesmas propriedades da classe Sprite do pygame
class hitbox (pygame.sprite.Sprite):
    # Inicializa (automaticamente) as características atribuídas ao objeto (definidas abaixo)
    def __init__(self, x, y, diretorio, id = None):
        # Chama o construtor da classe base Sprite para inicializar as propriedades padrão de um sprite
        pygame.sprite.Sprite.__init__(self)

        # O hitbox terá sua imagem baseada em um arquivo de imagem, que será direcionado através de um caminho(pathway) do diretório
        self.image = pygame.image.load(diretorio)

        # O retângulo que definirá o hitbox em si terá suas proporções baseadas na imagem recebida
        self.rect = self.image.get_rect()

        # A posição do hitbox na tela será dada por um x e um y
        self.rect.center = [x, y]

        # Define se está ativado ou não (caso o hitbox seja de uma bomba, ou outra coisa que precisa ser ativada)
        self.ativacao = None

        # Define a posição de spawn do hitbox (útil para balas)
        self.posicao_spawn = None

        # Define o contador do tempo de existência do hitbox, caso ele seja feito para desaparecer depois de um tempo
        self.tempo_existencia = 0

        self.id = id  # Define o id do hitbox (útil para identificar qual é o hitbox, caso tenha mais de um na tela)

    # Move horizontalmente a posição do hitbox na tela, em uma quantidade de pixels predefinida
    def mover_horizontal(self, qtd_pixels):
        self.rect.x += qtd_pixels
    
    # Move verticalmente a posição do hitbox na tela, em uma quantidade de pixels predefinida
    def mover_vertical(self, qtd_pixels):
        self.rect.y += qtd_pixels