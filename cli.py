import random

def quit_game():
    quit()

def flee():
    global in_fight
    d = random.choice('nswe')
    in_fight = False
    move(d)

def heal():
    hp = random.randint(0, 20)
    character['hp'] += hp
    print('Paranesid', hp)    

def attack():
    global in_fight

    print('Karu!!!')
    in_fight = True

    hit = random.randint(0, 20)
    character['hp'] -= hit
    print('Karu ründab', hit)

def get_location_str(l):
    return '_'.join([str(el) for el in l])

def move(d):
    global in_fight

    if in_fight == False:
        if d == 'n' and character['location'][0] != 0:
            character['location'][0] -= 1
        elif d == 's' and character['location'][0] != 3:
            character['location'][0] += 1
        elif d == 'w' and character['location'][1] != 0:
            character['location'][1] -= 1
        elif d == 'e' and character['location'][1] != 3:
            character['location'][1] += 1

    char_location_str = get_location_str(character['location'])
    if char_location_str in game_map.keys():
        if 'has_enemy' in game_map[char_location_str].keys():
            attack()
        if 'has_wizard' in game_map[char_location_str].keys():
            print('Siin ruumis saad oma tervist taastada')

character = {
    'location': [1, 2],
    'hp': 100
}

game_map = {
    '0_2': {
        'has_enemy': True,
    },
    '1_1': {
        'has_wizard': True,
    },
}

in_fight = False

while True:
    print('L:', get_location_str(character['location']), 'HP:', character['hp'])
    c = input('> ')
    if c in ['quit', 'q']:
        quit_game()
    elif c in ['north', 'n']:
        move('n')
    elif c in ['south', 's']:
        move('s')
    elif c in ['west', 'w']:
        move('w')
    elif c in ['east', 'e']:
        move('e')
    elif c in ['flee', 'f'] and in_fight:
        flee()
    elif c in ['heal', 'h']:
        heal()
