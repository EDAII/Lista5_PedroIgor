import pygame
from pygame.locals import *
from random import randint
from src import rb_tree
from src import get_all
from math import ceil
import copy

import time
def start():
    pygame.init()

    screen_size = (1070, 650)
    start_music = pygame.mixer.Sound("snd/start.wav")
    start_music.play(-1)

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Red Black Tree')

    w = 10
    card_pos = []
    # criando posições das cartas a serem ordenadas
    while w < 1060:
        card_pos.append((w, 50))
        w += 70

    myfont = pygame.font.SysFont('bold', 32)
    title_texts = []
    title_texts.append(myfont.render("Valores inseridos: ", False, (255,255,255)))
    title_texts.append(myfont.render("Red Black Tree: ", False, (255, 255, 255)))
    title_texts.append(myfont.render("Casos: ", False, (255, 255, 255)))
    insert_text = myfont.render("Insert", False, (0,0,0))
    cases_text = []



    # criando superfície das cartas
    card_skin = pygame.Surface((60, 90))
    card_skin.fill((255, 255, 255))
    card_skin_black = pygame.Surface((60, 90))
    card_skin_black.fill((0,0,0))
    card_skin_red = pygame.Surface((60, 90))
    card_skin_red.fill((255,0,0))
    insert_button = pygame.Surface((90,60))
    insert_button.fill((255,255,255))

    dict = {}
    sorts = []
    i_sort = 0



    ### iniciando rb tree
    tree = rb_tree.RedBlackTree()
    numbers = []
    nil = rb_tree.Node(None, 'NIL', None)
    tree_array= get_all.get_all(tree.root)

    input_box = pygame.Rect(875, 565, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 930 and pygame.mouse.get_pos()[1] >= 550:
                    if pygame.mouse.get_pos()[0] <= 1020 and pygame.mouse.get_pos()[1] <= 610:
                        rb_tree.CASOS.clear()
                        cases_text.clear()
                        if len(numbers)<=14:
                            try:
                                n = int(text)
                                if type(n) == int:
                                    if(int(text) not in numbers):
                                        tree.add(int(text))
                                        tree_array.clear()
                                        tree_array = get_all.get_all(tree.root)
                                        numbers.append(int(text))
                                        text = ''
                                        for c in rb_tree.CASOS:
                                            cases_text.append(myfont.render(c, False, (0, 0, 0)))
                            except Exception as e:
                                if text == '':
                                    while (True):
                                        x = randint(0, 100)
                                        if not x in numbers:
                                            tree.add(x)
                                            break
                                    tree_array.clear()
                                    tree_array = get_all.get_all(tree.root)
                                    numbers.append(x)
                                    for c in rb_tree.CASOS:
                                        cases_text.append(myfont.render(c, False, (0, 0, 0)))
                            text = ''

                mouse_position = (pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])
                if(len(numbers)>0):
                    if mouse_position[0] >= 10 and mouse_position[0] <= 140:
                        select_sound = pygame.mixer.Sound("snd/button-25.wav")
                        select_sound.play()
                        card_selected = ceil(mouse_position[1] / 70) - 1
                        count_card = 0
                        found_card = -1
                        for (posicao_x, posicao_y), valor in dict.items():
                            if count_card == card_selected:
                                found_card = valor
                                break
                            count_card+=1
                        if found_card >= 0:
                            tree.remove(found_card)
                            tree_array.clear()
                            tree_array = get_all.get_all(tree.root)
                            numbers.remove(found_card)
                            cases_text.clear()

                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                    # Change the current color of the input box.
                color = color_active if active else color_inactive



        screen.fill((150, 65, 200))
        screen.blit(title_texts[0], (10, 10))
        screen.blit(title_texts[1], (10, 150))
        screen.blit(title_texts[2], (10, 523))
        pos_j = 543
        for c in cases_text:
            screen.blit(c, (10, pos_j))
            pos_j += 20

        i = 0
        while i < len(numbers):
            dict[card_pos[i]] = copy.copy(numbers[i])
            show = card_skin_black
            screen.blit(show, card_pos[i])

            i += 1
        count_cards = 0
        for pos in card_pos:
            if count_cards ==len(numbers):
                break
            count_cards+=1
            number_surface = myfont.render(str(dict[pos]), False, (255, 255, 255))
            screen.blit(number_surface, (pos[0] + 2, pos[1] + 30))
        if tree_array != []:
            show = card_skin_black
            if not tree_array[0]:
                tree_array[0] = nil
            heap_parent = tree_array[0].value
            if tree_array[0].color == 'BLACK':
                show = card_skin_black
            elif tree_array[0].color == 'RED':
                show = card_skin_red
            screen.blit(show, (500,150))
            number_surface = myfont.render(str(heap_parent), False, (255, 255, 255))
            screen.blit(number_surface, (502, 180))

        if len(tree_array) > 1:
            if len(tree_array) >= 3:
                heap_children = tree_array[1:3]
                if heap_children[1].color == 'RED':
                    show1 = card_skin_red
                else:
                    show1 = card_skin_black
                if heap_children[0].color == 'RED':
                    show2 = card_skin_red
                else:
                    show2 = card_skin_black
                screen.blit(show1, (780, 240))
                number_surface = myfont.render(str(heap_children[1].value), False, (255, 255, 255))
                screen.blit(number_surface, (782, 270))
            else:
                show2 = card_skin_black
                heap_children = tree_array[1]
                if type(heap_children)!=list:
                    heap_children = [heap_children]
                if heap_children[0].color == 'BLACK':
                    show2 = card_skin_black
                elif heap_children[0].color == 'RED':
                    show2 = card_skin_red
            screen.blit(show2, (220, 240))
            number_surface = myfont.render(str(heap_children[0].value), False, (255, 255, 255))
            screen.blit(number_surface, (222, 270))

        if len(tree_array) > 3:
            if len(tree_array) >= 7:
                heap_g_children = tree_array[3:7]
            else:
                heap_g_children = tree_array[3:len(tree_array)]
            pos_x = 80
            h = 0
            for h in heap_g_children:
                show = card_skin_black
                if h:
                    if h.color == 'BLACK':
                        show = card_skin_black
                    elif h.color == 'RED':
                        show = card_skin_red
                    screen.blit(show, (pos_x, 335))
                    number_surface = myfont.render(str(h.value), False, (255, 255, 255))
                    screen.blit(number_surface, (pos_x+2, 365))
                pos_x+=280


        if len(tree_array) > 7:
            heap_g_g_children = tree_array[7:len(tree_array)]
            pos_x = 10
            for h in heap_g_g_children:
                show = card_skin_black
                if h:
                    if h.color == 'BLACK':
                        show = card_skin_black
                    elif h.color == 'RED':
                        show = card_skin_red
                    screen.blit(show, (pos_x, 430))
                    number_surface = myfont.render(str(h.value), False, (255, 255, 255))
                    screen.blit(number_surface, (pos_x + 2, 460))
                pos_x += 140
        pos_x = 10
        if i_sort > 0:
            for s in sorts:
                screen.blit(card_skin, (pos_x, 560))
                number_surface = myfont.render(str(s), False, (255, 255, 255))
                screen.blit(number_surface, (pos_x + 2, 590))
                pos_x+=70
        i_sort+=1
        if(len(numbers) <= 14):
            screen.blit(insert_button, (930, 550))
            screen.blit(insert_text, (942, 567))



        txt_surface = myfont.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(50, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()


        pygame.display.update()