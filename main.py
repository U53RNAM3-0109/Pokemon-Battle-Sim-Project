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
    grass = ['snivy', 'turtwig']
    water = ['oshawott', 'totodile']
    fire = ['tepig', 'cyndaquil']
    slot1 = grass.pop(rand.randint(0, 1))
    slot2 = fire.pop(rand.randint(0, 1))
    slot3 = water.pop(rand.randint(0, 1))

    team1 = [slot1, slot2, slot3]
    team2 = [grass[0], water[0], fire[0]]


    rand.shuffle(team1)
    rand.shuffle(team2)
    
    return team1,team2
    

team1, team2 = teamGenerate()
pygameImage = []


def game(team1, team2):
    #saves file names
    teamfile1 = []
    teamfile2 = []

    #create list with file names for images
    def file(team, teamfile, side):
        list = team
        for i in range(len(list)):
            photo = f"characters/{side}_{team[i]}.gif"
            teamfile.append(photo)
        return teamfile

    teamfile1 = file(team1, teamfile1, ('front'))
    teamfile2 = file(team2, teamfile2, ('back'))

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
        frame_num1 = 0
        frame_num2 = 0
        while run == True:
            clock.tick(10)
            screen.fill(0)
            background_image = pg.image.load("bg.png").convert()
            screen.blit(background_image, [0, 0])
            imageObject1.seek(frame_num1)
            imageObject2.seek(frame_num2)
            pygameImage1 = pilImageToSurface(
                imageObject1.convert('RGBA'))
            pygameImage2 = pilImageToSurface(
                imageObject2.convert('RGBA'))
            screen.blit(pygameImage1, (400, 230))
            screen.blit(pygameImage2, (100, 300))
            pg.display.update()
            frame_num1 = frame_num1 + 1
            frame_num2 = frame_num2 + 1
            if frame_num1 >= frame1:
                frame_num1 = 0
            if frame_num2 >= frame2:
                frame_num2 = 0


    match1_layout(teamfile1, teamfile2)

teamGenerate()
game(team1, team2)

def turnSystem():
    #check who is first
    #enter turn for char.
    #if player, present options
    #perform actions based on choice
    #else, choose random move
    #perform actions based on move
    #check for burn damage
    #perform next turn.
    pass

def speedCheck(poke1,poke2):
    #Returns pokemon with greatest speed
    if poke1['Speed'] > poke2['Speed']:
        return True
    elif poke1['Speed'] < poke2['Speed']:
        return False
    else:
        return rand.choice((True,False))




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





def give_poke_moves(pokemon, moves):
    for name in pokemon.keys():
        moveset = pokemon[name]['Moveset']
        pokemon[name]['Moveset'] = {}
        for move in moveset:
            pokemon[name]['Moveset'][move] = moves[move]
    return pokemon


#Create dictionaries
pokemon = load_pokemon_dict()
moves = load_moves_dict()
pokemon = give_poke_moves(pokemon, moves)


#NOTE
# Add a second set of stats to pokemon dictionary,
# to track current stats and statuses
# (after any effects are applied)