import pygame
from random import randint
pygame.init()

janela = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Jogo coletor')

janela_aberta = True

class Maça(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("maça.png")
        self.rect = self.image.get_rect()
        self.rect[0] = randint(20,450)
        self.rect[1] = 0

    def update(self):
        pass

    def velocidade(self):
        if pontos >= 30:
            self.rect[1] += 7
        else:
            self.rect[1] += 5

    def verificar(self):
        if self.rect[1] >= 420:
            self.rect[1] = randint(-200, -100)

    def voltar(self):
        self.rect[1] = randint(-200, -100)
        self.rect[0] = randint(20, 450)

maca_group = pygame.sprite.Group()
maca = Maça()
maca_group.add(maca)


class Melancia(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Melancia.png")
        self.rect = self.image.get_rect()
        self.rect[0] = randint(20, 450)
        self.rect[1] = -300

    def update(self):
        pass

    def velocidade(self):
        if pontos >= 30:
            self.rect[1] += 7
        else:
            self.rect[1] += 5

    def verificar(self):
        if self.rect[1] >= 420:
            self.rect[1] = -300

    def voltar(self):
        self.rect[1] = randint(-1000, -300)
        self.rect[0] = randint(20, 450)

melancia_group = pygame.sprite.Group()
melancia = Melancia()
melancia_group.add(melancia)


class Abacaxi(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("abacaxi.png")
        self.rect = self.image.get_rect()
        self.rect[0] = randint(20, 450)
        self.rect[1] = -700

    def update(self):
        pass

    def velocidade(self):
        if pontos >= 30:
            self.rect[1] += 7
        else:
            self.rect[1] += 5

    def verificar(self):
        if self.rect[1] >= 420:
            self.rect[1] = -700

    def voltar(self):
        self.rect[1] = randint(-500, -100)
        self.rect[0] = randint(20, 450)

abacaxi_group = pygame.sprite.Group()
abacaxi = Abacaxi()
abacaxi_group.add(abacaxi)

class Banana(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("banana.png")
        self.rect = self.image.get_rect()
        self.rect[0] = randint(20,450)
        self.rect[1] = -2000

    def update(self):
        pass

    def velocidade(self):
        if pontos >= 30:
            self.rect[1] += 7
        else:
            self.rect[1] += 5

    def verificar(self):
        if self.rect[1] >= 420:
            self.rect[1] = -2000

    def voltar(self):
        self.rect[1] = randint(-700, -300)
        self.rect[0] = randint(20, 450)

banana_group = pygame.sprite.Group()
banana = Banana()
banana_group.add(banana)

class Morango(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("morango.png")
        self.rect = self.image.get_rect()
        self.rect[0] = randint(20,450)
        self.rect[1] = -1000

    def update(self):
        pass

    def velocidade(self):
        if pontos >= 30:
            self.rect[1] += 7
        else:
            self.rect[1] += 5

    def verificar(self):
        if self.rect[1] >= 420:
            self.rect[1] = -1000

    def voltar(self):
        self.rect[1] = randint(-900, -300)
        self.rect[0] = randint(20, 450)

morango_group = pygame.sprite.Group()
morango = Morango()
morango_group.add(morango)


class Chao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("chao.png")
        self.rect = self.image.get_rect()
        self.rect[0] = 0
        self.rect[1] = 470

    def update(self):
        pass

chao_group = pygame.sprite.Group()
chao = Chao()
chao_group.add(chao)

class Cesta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("cesta.png")
        self.rect = self.image.get_rect()
        self.rect[0] = 225
        self.rect[1] = 410

    def update(self):
        pass
    def direita(self):
        self.rect[0] += 15

    def esquerda(self):
        self.rect[0] -= 15

cesta_group = pygame.sprite.Group()
cesta = Cesta()
cesta_group.add(cesta)

fundo = pygame.image.load("fundo2.png")

font = pygame.font.SysFont('arial black', 15)
texto = font.render("Pontos: ", True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (40,50)

vidas = 3

vida = font.render("Vidas: "+str(vidas), True,(255,255,255),(0,0,0))
pos_vida = texto.get_rect()
pos_vida.center = (40,75)

pontos = 0

while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT] :
        Cesta.direita(cesta)

    if comandos[pygame.K_LEFT] :
        Cesta.esquerda(cesta)

    if pygame.sprite.groupcollide(cesta_group, maca_group, False, False, ):
        pontos += 1
        Maça.voltar(maca)
        texto = font.render("Pontos: " + str(pontos), True, (255, 255, 255), (0, 0, 0))

    elif pygame.sprite.groupcollide(cesta_group, melancia_group, False, False, ):
        pontos += 1
        Melancia.voltar(melancia)
        texto = font.render("Pontos: " + str(pontos), True, (255, 255, 255), (0, 0, 0))

    elif pygame.sprite.groupcollide(cesta_group, abacaxi_group, False, False, ):
        pontos += 1
        Abacaxi.voltar(abacaxi)
        texto = font.render("Pontos: " + str(pontos), True, (255, 255, 255), (0, 0, 0))

    elif pygame.sprite.groupcollide(cesta_group, banana_group, False, False, ):
        pontos += 1
        Banana.voltar(banana)
        texto = font.render("Pontos: " + str(pontos), True, (255, 255, 255), (0, 0, 0))

    elif pygame.sprite.groupcollide(cesta_group, morango_group, False, False, ):
        pontos += 1
        Morango.voltar(morango)
        texto = font.render("Pontos: " + str(pontos), True, (255, 255, 255), (0, 0, 0))



    if pygame.sprite.groupcollide(chao_group, maca_group, False, False, ):
        vidas -= 1
        vida = font.render("Vidas: " + str(vidas), True, (255, 255, 255), (0, 0, 0))
        Maça.verificar(maca)
        
        if vidas == 0:
            print(f"Total de pontos: {pontos}")
            break

    elif pygame.sprite.groupcollide(chao_group, melancia_group, False, False, ):
        vidas -= 1
        vida = font.render("Vidas: " + str(vidas), True, (255, 255, 255), (0, 0, 0))
        Melancia.verificar(melancia)
        if vidas == 0:
            print("GAME OVER")
            print(f"Total de pontos: {pontos}")
            break

    elif pygame.sprite.groupcollide(chao_group, abacaxi_group, False, False, ):
        vidas -= 1
        vida = font.render("Vidas: " + str(vidas), True, (255, 255, 255), (0, 0, 0))
        Abacaxi.verificar(abacaxi)
        if vidas == 0:
            print("GAME OVER")
            print(f"Total de pontos: {pontos}")
            break

    elif pygame.sprite.groupcollide(chao_group, banana_group, False, False, ):
        vidas -= 1
        vida = font.render("Vidas: " + str(vidas), True, (255, 255, 255), (0, 0, 0))
        Banana.verificar(banana)
        if vidas == 0:
            print("GAME OVER")
            print(f"Total de pontos: {pontos}")
            break

    elif pygame.sprite.groupcollide(chao_group, morango_group, False, False, ):
        vidas -= 1
        vida = font.render("Vidas: " + str(vidas), True, (255, 255, 255), (0, 0, 0))
        Morango.verificar(morango)
        if vidas == 0:
            print("GAME OVER")
            print(f"Total de pontos: {pontos}")
            break



    Maça.velocidade(maca)
    Melancia.velocidade(melancia)
    Abacaxi.velocidade(abacaxi)
    Banana.velocidade(banana)
    Morango.velocidade(morango)

    pygame.display.update()
    janela.blit(fundo, (0, 0))

    morango_group.draw(janela)
    banana_group.draw(janela)
    abacaxi_group.draw(janela)

    janela.blit(texto, pos_texto)
    janela.blit(vida, pos_vida)

    cesta_group.draw(janela)
    melancia_group.draw(janela)
    maca_group.draw(janela)
    chao_group.draw(janela)


pygame.quit()