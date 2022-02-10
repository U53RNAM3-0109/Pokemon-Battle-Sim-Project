from PIL import Image
import pygame as pg
import random as rand
import csv
from pygame.locals import *

window_width = 800
window_height = 480
size = (window_width, window_height)
screen = pg.display.set_mode(size)

# Set title to the window
pg.display.set_caption("pokemon")
background_image = pg.image.load("bg.png").convert()
screen.blit(background_image, [0, 0])
pg.display.flip()


def teamGenerate():
    grass = ['snivy', 'rowlet']
    water = ['oshawott', 'totodile']
    fire = ['tepig', 'cyndaquil']
    slot1 = grass.pop(rand.randint(0, 1))
    slot2 = fire.pop(rand.randint(0, 1))
    slot3 = water.pop(rand.randint(0, 1))

    team1 = [slot1, slot2, slot3]
    team2 = [grass[0], water[0], fire[0]]

    #game(team1, team2)


#test
team1 = ['snivy', 'rowlet', 'oshawott']
team2 = ['totodile', 'tenpig', 'cyndaquil']
pygameImage = []


def game(team1, team2):
    #saves file names
    teamfile1 = ['characters/front_snivy.gif']
    teamfile2 = ['characters/back_totodile.gif']

    #create list with file names for images
    def file(team, teamfile, side):
        list = team
        for i in range(len(list)):
            photo = 'characters/', str(side) + str(team[i]) + '.gif'
            teamfile.append(photo)
        return teamfile

    file(team1, teamfile1, ('front_'))
    file(team2, teamfile2, ('back_'))

    def pilImageToSurface(pilImage):
        mode, size, data = pilImage.mode, pilImage.size, pilImage.tobytes()
        return pg.image.fromstring(data, size, mode).convert_alpha()

    #creates window
    screen = pg.display.set_mode((800, 480))
    # Set title to the window
    pg.display.set_caption("pokemon")
    #creates background
    background_image = pg.image.load("bg.png").convert()
    screen.blit(background_image, [0, 0])
    clock = pg.time.Clock()
    pg.display.flip()

    def match1_layout(teamfile1, teamfile2):
        imageObject1 = Image.open(teamfile1[0])
        imageObject2 = Image.open(teamfile2[0])
        run = True
        frame1 = imageObject1.n_frames
        frame2 = imageObject2.n_frames
        if frame1 < frame2:
            while run == True:
                for frame in range(0, imageObject1.n_frames):
                    clock.tick(10)
                    screen.fill(0)
                    background_image = pg.image.load("bg.png").convert()
                    screen.blit(background_image, [0, 0])
                    imageObject1.seek(frame)
                    imageObject2.seek(frame)
                    pygameImage1 = pilImageToSurface(
                        imageObject1.convert('RGBA'))
                    pygameImage2 = pilImageToSurface(
                        imageObject2.convert('RGBA'))
                    screen.blit(pygameImage1, (400, 230))
                    screen.blit(pygameImage2, (190, 340))
                    pg.display.update()
        else:
            while run == True:
                for frame in range(0, imageObject2.n_frames):
                    clock.tick(10)
                    screen.fill(0)
                    background_image = pg.image.load("bg.png").convert()
                    screen.blit(background_image, [0, 0])
                    imageObject1.seek(frame)
                    imageObject2.seek(frame)
                    pygameImage1 = pilImageToSurface(
                        imageObject1.convert('RGBA'))
                    pygameImage2 = pilImageToSurface(
                        imageObject2.convert('RGBA'))
                    screen.blit(pygameImage1, (400, 230))
                    screen.blit(pygameImage2, (190, 340))
                    pg.display.update()

    match1_layout(teamfile1, teamfile2)


#teamGenerate()
game(team1, team2)


def turnSystem():

    pass


def speedCheck():
    pass


def stat_modify():
    pass


def damage_calc(lvl, power, attack, defense, speed, stab, effective, burn):
    critChance = rand.randint(1, 256)
    if critChance < round(round((speed / 2)) / 256):
        crit = 2
    else:
        crit = 1
    roll = rand.uniform(0.85, 1)
    damage = round(
        ((((((2 * lvl) // 5) + 2) * power) * (attack // defense) // 50) + 2) *
        crit * roll * stab * effective * burn)
    print(damage)
    return damage


def load_pokemon_dict():
    with open('pokemon.csv', 'r') as file:
        keys = list(file.readline().strip().split(','))
        keys.pop(0)
        dictionary = {}
        for row in file:
            row = list(row.strip().split(','))
            dictionary[row[0]] = {}
            for i in range(len(keys)):
                upTo = i
                dictionary[row[0]][keys[i]] = row[i + 1]
            dictionary[row[0]][keys[upTo]] = row[i + 1::]

    return dictionary


def load_moves_dict():
    with open('moves.csv', 'r') as file:
        keys = list(file.readline().strip().split(','))
        keys[0] = keys[0].replace('#', '')
        dictionary = {}
        for row in file:
            row = list(row.strip().split(','))
            dictionary[row[0]] = {}
            for i in range(len(keys)):
                upTo = i
                dictionary[row[0]][keys[i]] = row[i]

    return dictionary


pokemon = load_pokemon_dict()
moves = load_moves_dict()


def give_poke_moves(pokemon, moves):
    for name in pokemon.keys():
        moveset = pokemon[name]['Moveset']
        pokemon[name]['Moveset'] = {}
        for move in moveset:
            pokemon[name]['Moveset'][move] = moves[move]
    return pokemon


pokemon = give_poke_moves(pokemon, moves)
#from main import load_moves_dict,give_poke_moves,load_moves_dict
