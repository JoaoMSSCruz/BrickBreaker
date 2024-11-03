def telainicial():
    import pygame
    import os


    #Janela

    WIDTH, HEIGHT = 800, 600
    janela = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption("Brick Breaker")

    #Imagens

    imagemfundo1 = pygame.image.load(os.path.join("background.png"))
    imagemfundo = pygame.transform.scale(imagemfundo1, (WIDTH, HEIGHT))
    imagem_levels1 = pygame.image.load(os.path.join("Levels.png"))
    imagem_exit1 = pygame.image.load(os.path.join("Exit_Button.png"))

    #Classes

    class Butões():
        def __init__(self, x, y, imagem, escala):
            width = imagem.get_width()
            height = imagem.get_height()
            self.imagem = pygame.transform.scale(imagem, (int(width * escala), int(height * escala)))
            self.rect = self.imagem.get_rect()
            self.rect.topleft = (x, y)
        def draw(self):
            clicado = False
            rato = pygame.mouse.get_pos()
            if self.rect.collidepoint(rato):
                if pygame.mouse.get_pressed()[0]:
                    clicado = True           
                
            janela.blit(self.imagem, (self.rect.x, self.rect.y))
            return clicado
    imagem_levels = Butões((WIDTH/2) - 140, HEIGHT/2 - 140, imagem_levels1, 0.7)
    imagem_exit = Butões((WIDTH/2) - 120, HEIGHT/2 + 15, imagem_exit1, 0.7)

    #Main Função

    def main():
        while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
            janela.blit(imagemfundo, (0, 0))
            if imagem_levels.draw() == True:
                telalevels()
                
            if imagem_exit.draw():
                pygame.quit()
            pygame.display.update()
    main()

###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################

def telalevels():
    import pygame
    import os
    pygame.font.init()

    branco = (3, 3, 3)

    #Recordes Iniciais
    file = open("tempos1.text", "a")
    file.write("59.59 \n")
    file.close()
    file = open("tempos2.text", "a")
    file.write("59.59 \n")
    file.close()
    file = open("tempos3.text", "a")
    file.write("59.59 \n")
    file.close()


    #Janela

    WIDTH, HEIGHT = 800, 600
    janela = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption("Levels")

    #Imagens

    imagemfundo1 = pygame.image.load(os.path.join("background.png"))
    imagemfundo = pygame.transform.scale(imagemfundo1, (WIDTH, HEIGHT))
    imagem_level1_1 = pygame.image.load(os.path.join("level1.png"))
    imagem_level2_1 = pygame.image.load(os.path.join("level2.png"))
    imagem_level3_1 = pygame.image.load(os.path.join("level3.png"))
    back1 = pygame.image.load(os.path.join("back.png"))


    #Classes

    class Butões():
        def __init__(self, x, y, imagem, escala):
            width = imagem.get_width()
            height = imagem.get_height()
            self.imagem = pygame.transform.scale(imagem, (int(width * escala), int(height * escala)))
            self.rect = self.imagem.get_rect()
            self.rect.topleft = (x, y)
            self.click = False
        def draw(self):
            clicado = False
            rato = pygame.mouse.get_pos()
            if self.rect.collidepoint(rato):
                if pygame.mouse.get_pressed()[0] and self.click == False:
                    self.click = True
                    clicado = True
                    
                
                if pygame.mouse.get_pressed()[0] == 0:
                    self.click = False
                
            janela.blit(self.imagem, (self.rect.x, self.rect.y))
            return clicado
    imagem_level1 = Butões(20, HEIGHT/2  - 40, imagem_level1_1, 0.5)
    imagem_level2 = Butões(285, HEIGHT/2 - 39, imagem_level2_1, 0.5)
    imagem_level3 = Butões(550, HEIGHT/2 - 41, imagem_level3_1, 0.5)
    back = Butões(25, 25, back1, 0.2)

    #Função de textos

    def texto1():   
        file = open("tempos1.text", "r")
        readthefile = file.readlines()
        menor_tempo = sorted(readthefile, reverse = False)
        fonte = pygame.font.SysFont("comicsansms", 22)
        texto = fonte.render("BEST SCORE: {}".format(menor_tempo[0]), True, branco)
        janela.blit(texto, (25, HEIGHT/2 + 50))

    def texto2():
        file = open("tempos2.text", "r")
        readthefile = file.readlines()
        menor_tempo = sorted(readthefile, reverse = False)
        fonte = pygame.font.SysFont("comicsansms", 22)
        texto = fonte.render("BEST SCORE: {}".format(menor_tempo[0]), True, branco)
        janela.blit(texto, (290, HEIGHT/2 + 50))

    def texto3():
        file = open("tempos3.text", "r")
        readthefile = file.readlines()
        menor_tempo = sorted(readthefile, reverse = False)
        fonte = pygame.font.SysFont("comicsansms", 22)
        texto = fonte.render("BEST SCORE: {}".format(menor_tempo[0]), True, branco)
        janela.blit(texto, (555, HEIGHT/2 + 50))


    #Main Função

    def main():
        while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
            janela.blit(imagemfundo, (0, 0))
            texto1()
            texto2()
            texto3()
            if back.draw():
                telainicial()
            if imagem_level1.draw():
                nivel1()
            if imagem_level2.draw():
                nivel2()
            if imagem_level3.draw():
                nivel3()
            
            pygame.display.update()
    main()

###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
def nivel1():
    import pygame  
    pygame.mixer.init() 
    import random  
    pygame.font.init() 
    import os

    #Cores predefinidas pelo pygame

    preto = (0, 0, 0) 
    branco = (255, 255, 255)
    vermelho = (245, 80, 80)
    verde = (102,205,0)
    azul = (0, 255, 255) 
    cinzento = (200,200,200)
    amarelo = (238, 238, 0)
    cor_fundo = (0,0,255)

    #Variáveis que serão utilizadas

    inicio = 1
    durante = 2
    derrota = 3
    vitoria = 4
    colunas = 10
    linhas = 6
    velocidadesx = [-4, -3, 3, 4] 
    FPS = 60 
    clock = pygame.time.Clock() 


    #Janela

    WIDTH, HEIGHT = 800, 600
    janela = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption("Brick Breaker")
    imagem_vitoria1 = pygame.image.load(os.path.join("imagem_vitoria.png")) 
    imagem_vitoria = pygame.transform.scale(imagem_vitoria1, (WIDTH, HEIGHT))

    #Classes

    class plataforma(): 
        def __init__(self):
            self.reset()
            self.vidas = 3
        def reset(self):
            self.width = WIDTH/6
            self.height = 20
            self.x = (WIDTH/2) - (self.width/2)
            self.y = HEIGHT - 75
            self.speed = 10
            self.direct = 0
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        def move(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_a] and self.rect.left > 0:
                self.direct = -1
                self.rect.x -= self.speed
            if key[pygame.K_d] and self.rect.right < WIDTH:
                self.direct = 1
                self.rect.x += self.speed

            
        def draw(self):
            pygame.draw.rect(janela, branco, self.rect)
            pygame.draw.rect(janela, preto, self.rect, 3)
    plataforma = plataforma()

    class bola():
        def __init__(self):
            self.width = 20
            self.height = 20
            self.x = (WIDTH/2) - (self.width/2)
            self.y = plataforma.y - self.height
            self.speedx =  random.choice(velocidadesx)
            self.speedy = -4
            self.maxspeedx = 5
            self.fim_do_jogo = 0
            self.lista = []
            self.intervalo_erro = 5
            self.maxspeedy = -5
            self.vitoria = 0
            self.som_bola = pygame.mixer.Sound("Audio_Bola.wav")
            self.rect = pygame.Rect(self.x, self.y , self.width, self.height)
        def move(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            #Colisão com Limites
            if self.rect.left < self.intervalo_erro:
                self.speedx *= -1
            if self.rect.right > WIDTH - self.intervalo_erro:
                self.speedx *= -1 
            if self.rect.top < 5:
                self.speedy *= -1
            if self.rect.bottom > HEIGHT - self.intervalo_erro:
                self.fim_do_jogo = 1
                plataforma.vidas -= 1
                
            #Colisão com Plataforma
            if self.rect.colliderect(plataforma):
                if abs(self.rect.bottom - plataforma.rect.top) < self.intervalo_erro:
                    self.som_bola.play()
                    self.speedy *= -1
                    if self.speedy > self.maxspeedy:
                        self.speedy += -1
                        self.intervalo_erro += 1
                    self.speedx += plataforma.direct
                    if self.speedx > self.maxspeedx:
                        self.speedx = self.maxspeedx
                    if self.speedx < -self.maxspeedx:
                        self.speedx = -self.maxspeedx
                if abs(self.rect.left - plataforma.rect.right) < self.intervalo_erro:
                    self.speedx *= -1
                    self.som_bola.play()
                if abs(self.rect.right - plataforma.rect.left) < self.intervalo_erro:
                    self.speedx *= -1
                    self.som_bola.play()
                
            #Colisão com Parede
            parede_destruida = 1
            numero_linhas = 0
            for linha in parede.blocos:
                lugar_bloco = 0
                for bloco in linha:
                    if self.rect.colliderect(bloco[0]):
                        if abs(self.rect.bottom - bloco[0].top) < self.intervalo_erro and self.speedy > 0:
                            self.speedy *= -1
                            pygame.mixer.music.load("bola_parede.wav")      
                            pygame.mixer.music.play()                        
                        if abs(self.rect.top - bloco[0].bottom) < self.intervalo_erro and self.speedy < 0:
                            self.speedy *= -1  
                            pygame.mixer.music.load("bola_parede.wav")      
                            pygame.mixer.music.play()                    
                        if abs(self.rect.right - bloco[0].left) < self.intervalo_erro and self.speedx > 0:
                            self.speedx *= -1
                            pygame.mixer.music.load("bola_parede.wav")      
                            pygame.mixer.music.play() 
                        if abs(self.rect.left - bloco[0].right) < self.intervalo_erro and self.speedx < 0:
                            self.speedx *= -1
                            pygame.mixer.music.load("bola_parede.wav")      
                            pygame.mixer.music.play()                     
                        parede.blocos[numero_linhas][lugar_bloco][0] = (0, 0, 0, 0)
                        parede.quantidade -= 1
                    if parede.blocos[numero_linhas][lugar_bloco][0] != (0, 0, 0, 0):
                        parede_destruida = 0                
                    lugar_bloco += 1
                numero_linhas += 1
            if parede_destruida == 1:
                self.vitoria = 1
                pygame.mixer.music.load("Musica_Vitoria.wav")      
                pygame.mixer.music.play()
        def draw(self):
            pygame.draw.rect(janela, cinzento, self.rect)
            pygame.draw.rect(janela, preto, self.rect, 2)
    bola = bola()

    class parede():
        def __init__(self):
            self.width = WIDTH / colunas
            self.height = 50
            self.quantidade = colunas * linhas

        def criar_parede(self):
            self.blocos = []
            bloco_individual = []
            for linha in range(linhas):
                linha_blocos = []
                self.y = linha * self.height + 40
                for coluna in range(colunas):
                    self.x = coluna * self.width
                    retangulo = pygame.Rect(self.x, self.y, self.width, self.height)
                    bloco_individual = [retangulo]
                    linha_blocos.append(bloco_individual)
                self.blocos.append(linha_blocos)
        


        def draw(self):
            for linha in self.blocos:
                for bloco in linha:
                    bloco_cor = verde
                    pygame.draw.rect(janela, bloco_cor, bloco[0])
                    pygame.draw.rect(janela, cor_fundo, (bloco[0]), 2)
                    
                    


    parede = parede()
    parede.criar_parede()

                

    #Funções

    #Janela inicial
    def janela_inicio():
        janela.fill(cor_fundo)
        plataforma.draw()
        bola.draw()
        parede.draw()
        texto_inicial()
        vidas()
        pygame.display.update()

    #Janela com o jogo a decorrer
    def janela_durante():
        janela.fill(cor_fundo)
        plataforma.draw()
        bola.draw()
        parede.draw()
        vidas()
        pygame.display.update()

    #Janela quando todos os blocos são destruidos
    def janela_final_vitoria():
        #janela.fill(cor_fundo)
        janela.blit(imagem_vitoria, (0, 0))
        texto_final_vitoria()
        pygame.display.update()

    #Janela quando o jogador perde as 3 vidas
    def janela_final_derrota():
        janela.fill(cor_fundo)
        plataforma.draw()
        bola.draw()
        parede.draw()
        vidas()
        texto_final_derrota()
        pygame.display.update()

    #Movimentos da plataforma e da bola
    def moves():
        plataforma.move()
        bola.move()

    #Texto no inicio de cada ronda
    def texto_inicial():
        fonte = pygame.font.SysFont("Normal", 30)
        texto = fonte.render("CLICK ANYWHERE TO START", True, branco)
        janela.blit(texto, (WIDTH/2 - 145, HEIGHT/2 + 100))

    #Texto quando todos os blocos são destruidos
    def texto_final_vitoria():
        fonte1 = pygame.font.SysFont("Normal", 80)
        texto1 = fonte1.render("YOU WON!", True, branco)
        janela.blit(texto1, (WIDTH/2 - 150, HEIGHT/2 - 60))
        fonte2 = pygame.font.SysFont("Normal", 30)
        texto2 = fonte2.render("CLICK ANYWHERE TO RESTART", True, branco)
        janela.blit(texto2, (WIDTH/2 - 160, HEIGHT/2 + 100))
        

    #Texto quando o jogador perde as vidas
    def texto_final_derrota():
        fonte1 = pygame.font.SysFont("Normal", 60)
        texto1 = fonte1.render("YOU LOST!", True, preto)
        janela.blit(texto1, (WIDTH/2 - 105, HEIGHT/2 - 75))
        texto2 = fonte1.render("BLOCKS REMAINING: {}".format(parede.quantidade), True, preto)
        janela.blit(texto2, (WIDTH/2 - 250, HEIGHT/2))
        fonte3 = pygame.font.SysFont("Normal", 30)
        texto3 = fonte3.render("CLICK ANYWHERE TO RESTART", True, branco)
        janela.blit(texto3, (WIDTH/2 - 150, HEIGHT/2 + 100))

    #Texto que indica as vidas do jogador
    def vidas():
        fonte = pygame.font.SysFont("Constantia", 40)
        texto = fonte.render("Lives: {}".format(plataforma.vidas), True, branco)
        janela.blit(texto, (WIDTH/2 - 80, 0))



        
    #Main Função

    def main():
        game_status = inicio
        score = 0
        while True:
            
            
            clock.tick(FPS)
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                pausa_nivel1()
            
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN and game_status == inicio:
                        game_status = durante
                    
                    if event.type == pygame.MOUSEBUTTONDOWN and game_status == derrota:
                        game_status = inicio
                        parede.quantidade = colunas*linhas
                        plataforma.vidas = 3
                        parede.criar_parede()
                    if event.type == pygame.MOUSEBUTTONDOWN and game_status == vitoria:
                        bola.vitoria = 0
                        game_status = inicio
                        bola.__init__()
                        plataforma.reset()
                        parede.criar_parede()
                        pygame.mixer.music.stop()
                        
            #Acontecimentos no inicio do jogo
            if game_status == inicio:
                janela_inicio()
            
            #Acontecimentos enquanto o jogo está a decorrer
            if game_status == durante:
                score = score + (1/FPS)
                minutos = score//60
                segundos = (score - (minutos*60))/100
                tempo1 = minutos + segundos
                tempo = round(tempo1, 2)
                moves()
                janela_durante()
                        
            #Acontecimentos cada vez que a bola vai para o limite inferior do mapa        
            if bola.fim_do_jogo == 1:
                bola.__init__()
                plataforma.reset()
                game_status = inicio
                    
            #Acontecimentos quando o player perde as 3 vidas
            if plataforma.vidas == 0:
                game_status = derrota
            if game_status == derrota:
                janela_final_derrota()
                    
            #Acontecimentos quando o player destroi todos os blocos    
            if bola.vitoria == 1:
                game_status = vitoria
            if game_status == vitoria:
                file = open("tempos1.text", "a")
                file.write("{}\n".format(tempo))
                file.close()
                janela_final_vitoria()
                plataforma.vidas = 3
            
            #Sons quando a bola vai para o limite inferior do mapa
            if plataforma.vidas == 3 and bola.rect.bottom > HEIGHT - 25:
                pygame.mixer.music.load("perda_de_vida.wav")      
                pygame.mixer.music.play()
            if plataforma.vidas == 2 and bola.rect.bottom > HEIGHT - 25:
                pygame.mixer.music.load("perda_de_vida.wav")      
                pygame.mixer.music.play()    
            if plataforma.vidas == 1 and bola.rect.bottom > HEIGHT - 20:
                pygame.mixer.music.load("Game_Over.wav")      
                pygame.mixer.music.play()
                
    main()

###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
def nivel2():
    import pygame  
    pygame.mixer.init() 
    import random  
    pygame.font.init() 
    import os

    #Cores predefinidas pelo pygame

    preto = (0, 0, 0) 
    branco = (255, 255, 255)
    vermelho = (245, 80, 80)
    verde = (102,205,0)
    azul = (0, 255, 255) 
    cinzento = (200,200,200)
    amarelo = (238, 238, 0)
    cor_fundo = (0,0,255)

    #Variáveis que serão utilizadas

    inicio = 1
    durante = 2
    derrota = 3
    vitoria = 4
    colunas = 10
    linhas = 6
    velocidadesx = [-4, -3, 3, 4] 
    FPS = 60 
    clock = pygame.time.Clock() 


    #Janela

    WIDTH, HEIGHT = 800, 600
    janela = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption("Brick Breaker")
    imagem_vitoria1 = pygame.image.load(os.path.join("imagem_vitoria.png")) 
    imagem_vitoria = pygame.transform.scale(imagem_vitoria1, (WIDTH, HEIGHT))

    #Classes

    class plataforma(): 
        def __init__(self):
            self.reset()
            self.vidas = 3
        def reset(self):
            self.width = WIDTH/6
            self.height = 20
            self.x = (WIDTH/2) - (self.width/2)
            self.y = HEIGHT - 75
            self.speed = 10
            self.direct = 0
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        def move(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_a] and self.rect.left > 0:
                self.direct = -1
                self.rect.x -= self.speed
            if key[pygame.K_d] and self.rect.right < WIDTH:
                self.direct = 1
                self.rect.x += self.speed

            
        def draw(self):
            pygame.draw.rect(janela, branco, self.rect)
            pygame.draw.rect(janela, preto, self.rect, 3)
    plataforma = plataforma()

    class bola():
        def __init__(self):
            self.width = 20
            self.height = 20
            self.x = (WIDTH/2) - (self.width/2)
            self.y = plataforma.y - self.height
            self.speedx =  random.choice(velocidadesx)
            self.speedy = -4
            self.maxspeedx = 5
            self.fim_do_jogo = 0
            self.lista = []
            self.intervalo_erro = 5
            self.maxspeedy = -5
            self.vitoria = 0
            self.som_bola = pygame.mixer.Sound("Audio_Bola.wav")
            self.rect = pygame.Rect(self.x, self.y , self.width, self.height)
        def move(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            #Colisão com Limites
            if self.rect.left < self.intervalo_erro:
                self.speedx *= -1
            if self.rect.right > WIDTH - self.intervalo_erro:
                self.speedx *= -1 
            if self.rect.top < 5:
                self.speedy *= -1
            if self.rect.bottom > HEIGHT - self.intervalo_erro:
                self.fim_do_jogo = 1
                plataforma.vidas -= 1
                
            #Colisão com Plataforma
            if self.rect.colliderect(plataforma):
                if abs(self.rect.bottom - plataforma.rect.top) < self.intervalo_erro:
                    self.som_bola.play()
                    self.speedy *= -1
                    if self.speedy > self.maxspeedy:
                        self.speedy += -1
                        self.intervalo_erro += 1
                    self.speedx += plataforma.direct
                    if self.speedx > self.maxspeedx:
                        self.speedx = self.maxspeedx
                    if self.speedx < -self.maxspeedx:
                        self.speedx = -self.maxspeedx
                if abs(self.rect.left - plataforma.rect.right) < self.intervalo_erro:
                    self.speedx *= -1
                    self.som_bola.play()
                if abs(self.rect.right - plataforma.rect.left) < self.intervalo_erro:
                    self.speedx *= -1
                    self.som_bola.play()
                
            #Colisão com Parede
            parede_destruida = 1
            numero_linhas = 0
            for linha in parede.blocos:
                lugar_bloco = 0
                for bloco in linha:
                    if self.rect.colliderect(bloco[0]):
                        if abs(self.rect.bottom - bloco[0].top) < self.intervalo_erro and self.speedy > 0:
                            self.speedy *= -1
                            pygame.mixer.music.load("bola_parede.wav")      
                            pygame.mixer.music.play()                        
                        if abs(self.rect.top - bloco[0].bottom) < self.intervalo_erro and self.speedy < 0:
                            self.speedy *= -1  
                            pygame.mixer.music.load("bola_parede.wav")      
                            pygame.mixer.music.play()                    
                        if abs(self.rect.right - bloco[0].left) < self.intervalo_erro and self.speedx > 0:
                            self.speedx *= -1
                            pygame.mixer.music.load("bola_parede.wav")      
                            pygame.mixer.music.play() 
                        if abs(self.rect.left - bloco[0].right) < self.intervalo_erro and self.speedx < 0:
                            self.speedx *= -1
                            pygame.mixer.music.load("bola_parede.wav")      
                            pygame.mixer.music.play() 
                        if parede.blocos[numero_linhas][lugar_bloco][1] > 1:
                            parede.blocos[numero_linhas][lugar_bloco][1] -= 1
                        else:
                            parede.blocos[numero_linhas][lugar_bloco][0] = (0, 0, 0, 0)
                            parede.quantidade -= 1
                    if parede.blocos[numero_linhas][lugar_bloco][0] != (0, 0, 0, 0):
                        parede_destruida = 0
                                
                    
                    lugar_bloco += 1
                numero_linhas += 1
            if parede_destruida == 1:
                self.vitoria = 1
                pygame.mixer.music.load("Musica_Vitoria.wav")      
                pygame.mixer.music.play()
        def draw(self):
            pygame.draw.rect(janela, cinzento, self.rect)
            pygame.draw.rect(janela, preto, self.rect, 2)
    bola = bola()

    class parede():
        def __init__(self):
            self.width = WIDTH / colunas
            self.height = 50
            self.quantidade = colunas * linhas

        def criar_parede(self):
            self.blocos = []
            bloco_individual = []
            for linha in range(linhas):
                linha_blocos = []
                self.y = linha * self.height + 40
                for coluna in range(colunas):
                    self.x = coluna * self.width
                    retangulo = pygame.Rect(self.x, self.y, self.width, self.height)
                    if  linha < 3:
                        durabilidade = 2
                    if 2 < linha < 6:
                        durabilidade = 1
                    bloco_individual = [retangulo, durabilidade]
                    linha_blocos.append(bloco_individual)
                self.blocos.append(linha_blocos)
        


        def draw(self):
            for linha in self.blocos:
                for bloco in linha:
                    if bloco[1] == 2:
                        bloco_cor = amarelo
                    if bloco[1] == 1:
                        bloco_cor = verde
                    pygame.draw.rect(janela, bloco_cor, bloco[0])
                    pygame.draw.rect(janela, cor_fundo, (bloco[0]), 2)
                    
                    


    parede = parede()
    parede.criar_parede()

                

    #Funções

    #Janela inicial
    def janela_inicio():
        janela.fill(cor_fundo)
        plataforma.draw()
        bola.draw()
        parede.draw()
        texto_inicial()
        vidas()
        pygame.display.update()

    #Janela com o jogo a decorrer
    def janela_durante():
        janela.fill(cor_fundo)
        plataforma.draw()
        bola.draw()
        parede.draw()
        vidas()
        pygame.display.update()

    #Janela quando todos os blocos são destruidos
    def janela_final_vitoria():
        #janela.fill(cor_fundo)
        janela.blit(imagem_vitoria, (0, 0))
        texto_final_vitoria()
        pygame.display.update()

    #Janela quando o jogador perde as 3 vidas
    def janela_final_derrota():
        janela.fill(cor_fundo)
        plataforma.draw()
        bola.draw()
        parede.draw()
        vidas()
        texto_final_derrota()
        pygame.display.update()

    #Movimentos da plataforma e da bola
    def moves():
        plataforma.move()
        bola.move()

    #Texto no inicio de cada ronda
    def texto_inicial():
        fonte = pygame.font.SysFont("Normal", 30)
        texto = fonte.render("CLICK ANYWHERE TO START", True, branco)
        janela.blit(texto, (WIDTH/2 - 145, HEIGHT/2 + 100))

    #Texto quando todos os blocos são destruidos
    def texto_final_vitoria():
        fonte1 = pygame.font.SysFont("Normal", 80)
        texto1 = fonte1.render("YOU WON!", True, branco)
        janela.blit(texto1, (WIDTH/2 - 150, HEIGHT/2 - 60))
        fonte2 = pygame.font.SysFont("Normal", 30)
        texto2 = fonte2.render("CLICK ANYWHERE TO RESTART", True, branco)
        janela.blit(texto2, (WIDTH/2 - 160, HEIGHT/2 + 100))
        

    #Texto quando o jogador perde as vidas
    def texto_final_derrota():
        fonte1 = pygame.font.SysFont("Normal", 60)
        texto1 = fonte1.render("YOU LOST!", True, preto)
        janela.blit(texto1, (WIDTH/2 - 105, HEIGHT/2 - 75))
        texto2 = fonte1.render("BLOCKS REMAINING: {}".format(parede.quantidade), True, preto)
        janela.blit(texto2, (WIDTH/2 - 250, HEIGHT/2))
        fonte3 = pygame.font.SysFont("Normal", 30)
        texto3 = fonte3.render("CLICK ANYWHERE TO RESTART", True, branco)
        janela.blit(texto3, (WIDTH/2 - 150, HEIGHT/2 + 100))

    #Texto que indica as vidas do jogador
    def vidas():
        fonte = pygame.font.SysFont("Constantia", 40)
        texto = fonte.render("Lives: {}".format(plataforma.vidas), True, branco)
        janela.blit(texto, (WIDTH/2 - 80, 0))

        
    #Main Função

    def main():
        game_status = inicio
        score = 0
            
        while True:
            clock.tick(FPS)
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                pausa_nivel2()
            
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN and game_status == inicio:
                        game_status = durante
                    
                    if event.type == pygame.MOUSEBUTTONDOWN and game_status == derrota:
                        game_status = inicio
                        parede.quantidade = colunas*linhas
                        plataforma.vidas = 3
                        parede.criar_parede()
                    if event.type == pygame.MOUSEBUTTONDOWN and game_status == vitoria:
                        bola.vitoria = 0
                        game_status = inicio
                        bola.__init__()
                        plataforma.reset()
                        parede.criar_parede()
                        pygame.mixer.music.stop()
                        
            #Acontecimentos no inicio do jogo
            if game_status == inicio:
                janela_inicio()
            
            #Acontecimentos enquanto o jogo está a decorrer
            if game_status == durante:
                score = score + (1/FPS)
                minutos = score//60
                segundos = (score - (minutos*60))/100
                tempo1 = minutos + segundos
                tempo = round(tempo1, 2)
                moves()
                janela_durante()
                        
            #Acontecimentos cada vez que a bola vai para o limite inferior do mapa        
            if bola.fim_do_jogo == 1:
                bola.__init__()
                plataforma.reset()
                game_status = inicio
                    
            #Acontecimentos quando o player perde as 3 vidas
            if plataforma.vidas == 0:
                game_status = derrota
            if game_status == derrota:
                janela_final_derrota()
            
                
                
            #Acontecimentos quando o player destroi todos os blocos    
            if bola.vitoria == 1:
                game_status = vitoria
            if game_status == vitoria:
                file = open("tempos2.text", "a")
                file.write("{}\n".format(tempo))
                file.close()
                janela_final_vitoria()
                plataforma.vidas = 3
            
            #Sons quando a bola vai para o limite inferior do mapa
            if plataforma.vidas == 3 and bola.rect.bottom > HEIGHT - 25:
                pygame.mixer.music.load("perda_de_vida.wav")      
                pygame.mixer.music.play()
            if plataforma.vidas == 2 and bola.rect.bottom > HEIGHT - 25:
                pygame.mixer.music.load("perda_de_vida.wav")      
                pygame.mixer.music.play()    
            if plataforma.vidas == 1 and bola.rect.bottom > HEIGHT - 20:
                pygame.mixer.music.load("Game_Over.wav")      
                pygame.mixer.music.play()
                
    main()

###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################

def nivel3():
    import pygame   
    import random
    import os
    pygame.mixer.init()    
    pygame.font.init() 


    #Cores predefinidas pelo pygame

    preto = (0, 0, 0) 
    branco = (255, 255, 255)
    vermelho = (245, 80, 80)
    verde = (102,205,0)
    azul = (0, 255, 255) 
    cinzento = (200,200,200)
    amarelo = (238, 238, 0)
    cor_fundo = (0,0,255)

    #Variáveis que serão utilizadas

    inicio = 1   
    durante = 2
    derrota = 3
    vitoria = 4
    colunas = 10    
    linhas = 6 
    velocidadesx = [-4, -3, 3, 4]   
    FPS = 60    
    clock = pygame.time.Clock() 


    #Janela

    WIDTH, HEIGHT = 800, 600   
    janela = pygame.display.set_mode((WIDTH, HEIGHT))   
    pygame.display.set_caption("Brick Breaker")     
    imagem_vitoria1 = pygame.image.load(os.path.join("imagem_vitoria.png"))     
    imagem_vitoria = pygame.transform.scale(imagem_vitoria1, (WIDTH, HEIGHT))    
    #Classes

    class plataforma():     
        def __init__(self):    
            self.reset()
            self.vidas = 3     
        def reset(self):
            self.width = WIDTH/6    
            self.height = 20    
            self.x = (WIDTH/2) - (self.width/2)     
            self.y = HEIGHT - 75
            self.speed = 10     
            self.direct = 0    
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)    
        def move(self): 
            key = pygame.key.get_pressed()      
            if key[pygame.K_a] and self.rect.left > 0:  
                self.direct = -1    
                self.rect.x -= self.speed   
            if key[pygame.K_d] and self.rect.right < WIDTH: 
                self.direct = 1     
                self.rect.x += self.speed  

            
        def draw(self):
            pygame.draw.rect(janela, branco, self.rect)     
            pygame.draw.rect(janela, preto, self.rect, 3)    
    plataforma = plataforma()   

    class bola():
        def __init__(self):     
            self.width = 20     
            self.height = 20    
            self.x = (WIDTH/2) - (self.width/2)     
            self.y = plataforma.y - self.height
            self.speedx =  random.choice(velocidadesx)     
            self.speedy = -4    
            self.maxspeedx = 5     
            self.fim_do_jogo = 0         
            self.intervalo_erro = 5     
            self.maxspeedy = -5     
            self.vitoria = 0    
            self.som_bola = pygame.mixer.Sound("Audio_Bola.wav")    
            self.rect = pygame.Rect(self.x, self.y , self.width, self.height)   
        def move(self):
            self.rect.x += self.speedx      
            self.rect.y += self.speedy      
            #Colisão com Limites
            if self.rect.left < self.intervalo_erro:    
                self.speedx *= -1   
            if self.rect.right > WIDTH - self.intervalo_erro:   
                self.speedx *= -1   
            if self.rect.top < 5:   
                self.speedy *= -1   
            if self.rect.bottom > HEIGHT - self.intervalo_erro:     
                self.fim_do_jogo = 1   
                plataforma.vidas -= 1 
                
            #Colisão com Plataforma
            if self.rect.colliderect(plataforma):  
                if abs(self.rect.bottom - plataforma.rect.top) < self.intervalo_erro: 
                    self.som_bola.play()    
                    self.speedy *= -1  
                    if self.speedy > self.maxspeedy:    
                        self.speedy += -1    
                        self.intervalo_erro += 1   
                    self.speedx += plataforma.direct    
                    if self.speedx > self.maxspeedx:    
                        self.speedx = self.maxspeedx
                    if self.speedx < -self.maxspeedx:
                        self.speedx = -self.maxspeedx
                if abs(self.rect.left - plataforma.rect.right) < self.intervalo_erro:    
                    self.speedx *= -1   
                    self.som_bola.play()    
                if abs(self.rect.right - plataforma.rect.left) < self.intervalo_erro:    
                    self.speedx *= -1   
                    self.som_bola.play()    
                
            #Colisão com Parede
            parede_destruida = 1    
            numero_linhas = 0   
            for linha in parede.blocos:    
                lugar_bloco = 0     
                for bloco in linha:     
                    if self.rect.colliderect(bloco[0]):     
                        if abs(self.rect.bottom - bloco[0].top) < self.intervalo_erro and self.speedy > 0:  
                            self.speedy *= -1   
                            pygame.mixer.music.load("bola_parede.wav")  
                            pygame.mixer.music.play()               
                        if abs(self.rect.top - bloco[0].bottom) < self.intervalo_erro and self.speedy < 0: 
                            self.speedy *= -1  
                            pygame.mixer.music.load("bola_parede.wav")      
                            pygame.mixer.music.play()                    
                        if abs(self.rect.right - bloco[0].left) < self.intervalo_erro and self.speedx > 0: 
                            self.speedx *= -1   
                            pygame.mixer.music.load("bola_parede.wav")      
                            pygame.mixer.music.play() 
                        if abs(self.rect.left - bloco[0].right) < self.intervalo_erro and self.speedx < 0:   
                            self.speedx *= -1   
                            pygame.mixer.music.load("bola_parede.wav")      
                            pygame.mixer.music.play() 
                        if parede.blocos[numero_linhas][lugar_bloco][1] > 1:    
                            parede.blocos[numero_linhas][lugar_bloco][1] -= 1   
                        else:
                            parede.blocos[numero_linhas][lugar_bloco][0] = (0, 0, 0, 0)     
                            parede.quantidade -= 1  
                    if parede.blocos[numero_linhas][lugar_bloco][0] != (0, 0, 0, 0):    
                        parede_destruida = 0    
                                
                    
                    lugar_bloco += 1    
                numero_linhas += 1
            if parede_destruida == 1:   
                self.vitoria = 1    
                pygame.mixer.music.load("Musica_Vitoria.wav")     
                pygame.mixer.music.play()   
        def draw(self):     
            pygame.draw.rect(janela, cinzento, self.rect)   
            pygame.draw.rect(janela, preto, self.rect, 2)   
    bola = bola()   

    class parede():    
        def __init__(self):     
            self.width = WIDTH / colunas   
            self.height = 50    
            self.quantidade = colunas * linhas  

        def criar_parede(self):
            self.blocos = []    
            bloco_individual = []   
            for linha in range(linhas):     
                linha_blocos = []   
                self.y = linha * self.height + 40   
                for coluna in range(colunas):   
                    self.x = coluna * self.width    
                    retangulo = pygame.Rect(self.x, self.y, self.width, self.height)   
                    if linha < 2:   
                        durabilidade = 3   
                    if  1 < linha < 4: 
                        durabilidade = 2    
                    if 3 < linha < 6:   
                        durabilidade = 1    
                    bloco_individual = [retangulo, durabilidade]    
                    linha_blocos.append(bloco_individual)   
                self.blocos.append(linha_blocos)    
        


        def draw(self):     
            for linha in self.blocos:   
                for bloco in linha:     
                    if bloco[1] == 3:   
                        bloco_cor = vermelho    
                    if bloco[1] == 2:   
                        bloco_cor = amarelo     
                    if bloco[1] == 1:   
                        bloco_cor = verde   
                    pygame.draw.rect(janela, bloco_cor, bloco[0])   
                    pygame.draw.rect(janela, cor_fundo, (bloco[0]), 2)  
                    
                    


    parede = parede()   
    parede.criar_parede()   

                

    #Funções

    #Janela inicial
    def janela_inicio():
        janela.fill(cor_fundo)  
        plataforma.draw()   
        bola.draw()    
        parede.draw()   
        texto_inicial() 
        vidas()     
        pygame.display.update()     

    #Janela com o jogo a decorrer
    def janela_durante():   
        janela.fill(cor_fundo)
        plataforma.draw()
        bola.draw()
        parede.draw()
        vidas()
        pygame.display.update()

    #Janela quando todos os blocos são destruidos
    def janela_final_vitoria():
        janela.blit(imagem_vitoria, (0, 0))     
        texto_final_vitoria()   
        pygame.display.update()

    #Janela quando o jogador perde as 3 vidas
    def janela_final_derrota():
        janela.fill(cor_fundo)
        plataforma.draw()
        bola.draw()
        parede.draw()
        vidas()
        texto_final_derrota()   
        pygame.display.update()

    #Movimentos da plataforma e da bola
    def moves():    
        plataforma.move()   
        bola.move()     

    #Texto no inicio de cada ronda
    def texto_inicial():
        fonte = pygame.font.SysFont("Normal", 30)   
        texto = fonte.render("CLICK ANYWHERE TO START", True, branco)   
        janela.blit(texto, (WIDTH/2 - 145, HEIGHT/2 + 100))     

    #Texto quando todos os blocos são destruidos
    def texto_final_vitoria():
        fonte1 = pygame.font.SysFont("Normal", 80)
        texto1 = fonte1.render("YOU WON!", True, branco)
        janela.blit(texto1, (WIDTH/2 - 150, HEIGHT/2 - 60))
        fonte2 = pygame.font.SysFont("Normal", 30)
        texto2 = fonte2.render("CLICK ANYWHERE TO RESTART", True, branco)
        janela.blit(texto2, (WIDTH/2 - 160, HEIGHT/2 + 100))      
        

    #Texto quando o jogador perde as vidas
    def texto_final_derrota():
        fonte1 = pygame.font.SysFont("Normal", 60)
        texto1 = fonte1.render("YOU LOST!", True, preto)
        janela.blit(texto1, (WIDTH/2 - 105, HEIGHT/2 - 75))
        texto2 = fonte1.render("BLOCKS REMAINING: {}".format(parede.quantidade), True, preto)
        janela.blit(texto2, (WIDTH/2 - 250, HEIGHT/2))
        fonte3 = pygame.font.SysFont("Normal", 30)
        texto3 = fonte3.render("CLICK ANYWHERE TO RESTART", True, branco)
        janela.blit(texto3, (WIDTH/2 - 150, HEIGHT/2 + 100))    

    #Texto que indica as vidas do jogador
    def vidas():
        fonte = pygame.font.SysFont("Constantia", 40)
        texto = fonte.render("Lives: {}".format(plataforma.vidas), True, branco)
        janela.blit(texto, (WIDTH/2 - 80, 0))      

        
    #Main Função

    def main():
        game_status = inicio    
        score = 0    
        while True:
            clock.tick(FPS)     
            

            key = pygame.key.get_pressed()  
            if key[pygame.K_ESCAPE]:    
                pausa_nivel3()     
            
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:   
                        pygame.quit()   
                    if event.type == pygame.MOUSEBUTTONDOWN and game_status == inicio:  
                        game_status = durante   
                    
                    if event.type == pygame.MOUSEBUTTONDOWN and game_status == derrota:
                        game_status = inicio
                        parede.quantidade = colunas*linhas
                        plataforma.vidas = 3
                        parede.criar_parede()
                    if event.type == pygame.MOUSEBUTTONDOWN and game_status == vitoria:
                        bola.vitoria = 0
                        game_status = inicio
                        bola.__init__()
                        plataforma.reset()
                        parede.criar_parede()
                        pygame.mixer.music.stop()
                        
            #Acontecimentos no inicio do jogo
            if game_status == inicio:
                janela_inicio()
            
            #Acontecimentos enquanto o jogo está a decorrer
            if game_status == durante:
                score = score + (1/FPS)
                minutos = score//60
                segundos = (score - (minutos*60))/100
                tempo1 = minutos + segundos
                tempo = round(tempo1, 2)
                moves()
                janela_durante()
                        
            #Acontecimentos cada vez que a bola vai para o limite inferior do mapa        
            if bola.fim_do_jogo == 1:
                bola.__init__()
                plataforma.reset()
                game_status = inicio
                    
            #Acontecimentos quando o player perde as 3 vidas
            if plataforma.vidas == 0:
                game_status = derrota
            if game_status == derrota:
                janela_final_derrota()
            
                
                
            #Acontecimentos quando o player destroi todos os blocos    
            if bola.vitoria == 1:
                game_status = vitoria
            if game_status == vitoria:
                file = open("tempos3.text", "a")
                file.write("{}\n".format(tempo))
                file.close()
                janela_final_vitoria()
                plataforma.vidas = 3
            
            #Sons quando a bola vai para o limite inferior do mapa
            if plataforma.vidas == 3 and bola.rect.bottom > HEIGHT - 25:
                pygame.mixer.music.load("perda_de_vida.wav")      
                pygame.mixer.music.play()
            if plataforma.vidas == 2 and bola.rect.bottom > HEIGHT - 25:
                pygame.mixer.music.load("perda_de_vida.wav")      
                pygame.mixer.music.play()    
            if plataforma.vidas == 1 and bola.rect.bottom > HEIGHT - 20:
                pygame.mixer.music.load("Game_Over.wav")      
                pygame.mixer.music.play()
                
    main()

###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################

def pausa_nivel1():
    import pygame
    import os


    #Janela

    WIDTH, HEIGHT = 800, 600
    janela = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption("Brick Breaker")

    #Imagens

    imagemfundo1 = pygame.image.load(os.path.join("background.png"))
    imagemfundo = pygame.transform.scale(imagemfundo1, (WIDTH, HEIGHT))
    restart1 = pygame.image.load(os.path.join("restart.png"))
    menu2 = pygame.image.load(os.path.join("menu.png"))
    menu1 = pygame.transform.scale(menu2, (400, 200))

    #Classes

    class Botões():
        def __init__(self, x, y, imagem, escala):
            width = imagem.get_width()
            height = imagem.get_height()
            self.imagem = pygame.transform.scale(imagem, (int(width * escala), int(height * escala)))
            self.rect = self.imagem.get_rect()
            self.rect.topleft = (x, y)
        def draw(self):
            clicado = False
            rato = pygame.mouse.get_pos()
            if self.rect.collidepoint(rato):
                if pygame.mouse.get_pressed()[0]: 
                    clicado = True
                
            janela.blit(self.imagem, (self.rect.x, self.rect.y))
            return clicado
    restart = Botões(50, HEIGHT/2- 50, restart1, 0.35)
    menu = Botões(515, HEIGHT/2 - 55, menu1, 0.55)

    #Main Função

    def main():
        while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
            janela.blit(imagemfundo, (0, 0))
            if restart.draw() == True:
                nivel1()
                
            if menu.draw():
                telainicial()
            pygame.display.update()
    main()

###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################

def pausa_nivel2():
    import pygame
    import os


    #Janela

    WIDTH, HEIGHT = 800, 600
    janela = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption("Brick Breaker")

    #Imagens

    imagemfundo1 = pygame.image.load(os.path.join("background.png"))
    imagemfundo = pygame.transform.scale(imagemfundo1, (WIDTH, HEIGHT))
    restart1 = pygame.image.load(os.path.join("restart.png"))
    menu2 = pygame.image.load(os.path.join("menu.png"))
    menu1 = pygame.transform.scale(menu2, (400, 200))

    #Classes

    class Botões():
        def __init__(self, x, y, imagem, escala):
            width = imagem.get_width()
            height = imagem.get_height()
            self.imagem = pygame.transform.scale(imagem, (int(width * escala), int(height * escala)))
            self.rect = self.imagem.get_rect()
            self.rect.topleft = (x, y)
        def draw(self):
            clicado = False
            rato = pygame.mouse.get_pos()
            if self.rect.collidepoint(rato):
                if pygame.mouse.get_pressed()[0]:
                    clicado = True

            janela.blit(self.imagem, (self.rect.x, self.rect.y))
            return clicado
    restart = Botões(50, HEIGHT/2- 50, restart1, 0.35)
    menu = Botões(515, HEIGHT/2 - 55, menu1, 0.55)

    #Main Função

    def main():
        while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
            janela.blit(imagemfundo, (0, 0))
            if restart.draw() == True:
                nivel2()
                
            if menu.draw():
                telainicial()
            pygame.display.update()
    main()

###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################

def pausa_nivel3():
    import pygame
    import os


    #Janela

    WIDTH, HEIGHT = 800, 600
    janela = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption("Brick Breaker")

    #Imagens

    imagemfundo1 = pygame.image.load(os.path.join("background.png"))
    imagemfundo = pygame.transform.scale(imagemfundo1, (WIDTH, HEIGHT))
    restart1 = pygame.image.load(os.path.join("restart.png"))
    menu2 = pygame.image.load(os.path.join("menu.png"))
    menu1 = pygame.transform.scale(menu2, (400, 200))

    #Classes

    class Botões():
        def __init__(self, x, y, imagem, escala):
            width = imagem.get_width()
            height = imagem.get_height()
            self.imagem = pygame.transform.scale(imagem, (int(width * escala), int(height * escala)))
            self.rect = self.imagem.get_rect()
            self.rect.topleft = (x, y)
        def draw(self):
            clicado = False
            rato = pygame.mouse.get_pos()
            if self.rect.collidepoint(rato):
                if pygame.mouse.get_pressed()[0]:
                    clicado = True
                    
            janela.blit(self.imagem, (self.rect.x, self.rect.y))
            return clicado
    restart = Botões(50, HEIGHT/2- 50, restart1, 0.35)
    menu = Botões(515, HEIGHT/2 - 55, menu1, 0.55)

    #Main Função

    def main():
        while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
            janela.blit(imagemfundo, (0, 0))
            if restart.draw() == True:
                nivel3()
                
            if menu.draw():
                telainicial()
            pygame.display.update()
    main()


telainicial()