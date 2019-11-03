import pygame
from pygame.locals import *
from src import start_game
def begin():
    pygame.init()

    init_sound = pygame.mixer.Sound("snd/init.wav")
    init_sound.play(-1)

    screen_size = (710, 512)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Red Black Tree')
    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    my_font = pygame.font.SysFont('bold', 80)
    start_font = pygame.font.SysFont('bold', 22)

    start_button_skin = pygame.Surface((50, 35))
    start_button_skin.fill((255, 255, 255))
    start_count = 0
    clock = pygame.time.Clock()

    # INSTRUCTIONS
    ins_font = pygame.font.SysFont('bold', 50)
    ins_texts = []
    ins_texts.append(ins_font.render("Será feita a ordenação de 15 valores", False, (255, 255, 255)))
    ins_texts.append(ins_font.render("por meio do algoritmo Heap Sort", False, (255, 255, 255)))
    ins_texts.append(ins_font.render("É possível visualizar no topo o vetor", False, (255, 255, 255)))
    ins_texts.append(ins_font.render("original criado de forma aleatória,", False, (255, 255, 255)))
    ins_texts.append(ins_font.render("ao centro o Max Heap de cada iteração", False, (255, 255, 255)))
    ins_texts.append(ins_font.render("e logo abaixo o vetor ordenado", False, (255, 255, 255)))
    ins_texts.append(ins_font.render("adicionando a raiz do Heap a cada passo.", False, (255, 255, 255)))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 600 and pygame.mouse.get_pos()[1]>=390:
                    if pygame.mouse.get_pos()[0] <= 647 and pygame.mouse.get_pos()[1]<=425:
                        init_sound.stop()
                        start_game.start()
        pygame.display.update()
        screen.fill((150, 65, 200))
        text_surface = my_font.render("Heap Sort", False, (255, 255, 255))
        start_text_surface = start_font.render("START", False, (255, 0, 0))
        screen.blit(text_surface, (80,10))
        screen.blit(start_button_skin, (599, 390))
        #SHOW INSTRUCTIONS:
        #image = pygame.image.load('img/game.png')
        #image = pygame.transform.scale(image, (440, 320))
        pos_y = 60
        i = 1
        for ins in ins_texts:
            screen.blit(ins, (20,pos_y))
            if i == 2:
                pos_y+=20
            i += 1
            pos_y+=40
        #screen.blit(image, (130,120))
        #screen.blit(ins_texts[-1], (100, 442))
        if start_count > 100:
            screen.blit(start_text_surface, (600, 400))
        if start_count > 200:
            start_count = 0
        start_count+=1

        clock.tick(120)