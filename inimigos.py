from Hitabox import hitbox
import constantes

class inimigo_horizontal(hitbox):
    def __init__(self, x, y, diretorio, id=None):
        super().__init__(x, y, diretorio, id)

        # Define a velocidade do inimigo
        self.velocidade = 10

        # Define a direção do movimento do inimigo (1 = direita, -1 = esquerda)
        self.direcao = 1

        # Define a quantidade de pixels que o inimigo deve se mover para baixo
        self.descer = 0

    def mover(self):
        # Move o inimigo horizontalmente de acordo com sua direção e velocidade
        self.mover_horizontal(self.velocidade * self.direcao)
        self.mover_vertical(3)
        # Inverte a direção se o inimigo atingir as bordas da tela
        if self.rect.left < 0 or self.rect.right > constantes.X:
            self.direcao *= -1

    def update(self):
        # Atualiza o movimento do inimigo
        self.mover()

class kamikaze(hitbox):
    def __init__(self, x, y, diretorio, id=None):
        super().__init__(x, y, diretorio, id)

        # Define a velocidade do inimigo
        self.velocidade = 10

    def mover(self):
        # Move o inimigo horizontalmente de acordo com sua direção e velocidade
        self.mover_vertical(self.velocidade)

        # destroi o inimigo se ele sair da tela
        if self.rect.top > constantes.Y + 30:
            self.kill()

    def update(self):
        # Atualiza o movimento do inimigo
        self.mover()
