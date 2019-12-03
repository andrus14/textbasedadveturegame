import random, time, threading

def read_command():
    
    global commands, command_aliases

    c = input('> ')
    if c in command_aliases.keys():
        c = command_aliases[c]

    while c not in commands.keys():
        print('Error: command not found!')

        c = input('> ')
        if c in command_aliases.keys():
            c = command_aliases[c]

    return c

def quit_game(args):
    quit()

def hit(target):
    global character

    if target == 'character':

        while character['hp'] > 0:
            power = random.randint(0, 20)
            character['hp'] -= power
            print('Karu ründab', str(power) + '!')
            time.sleep(0.5)

def move(args):
    global character, game_map
    m = args[0]
    if m == 'n' and character['location'][0] != 0:
        character['location'][0] -= 1
    elif m == 's' and character['location'][0] != 3:
        character['location'][0] += 1
    if m == 'w' and character['location'][1] != 0:
        character['location'][1] -= 1
    if m == 'e' and character['location'][1] != 3:
        character['location'][1] += 1

    print('move', args[0])

    char_location_str = get_room_key(character['location'])
    if char_location_str in game_map:
        if 'has_enemy' in game_map[char_location_str].keys():
            print('Karu!!!')
            bear = threading.Thread(target=hit, args=('character',))
            bear.start()

def get_room_key( location ):
    return '_'.join([str(el) for el in location])

def flee(args):
    move(random.choice('nesw'))

def available_commands(args):
    global commands
    print('Available commands: ' + ' '.join(commands.keys()))

commands = {
    'quit': {'function': 'quit_game', 'args': None},
    'help': {'function': 'available_commands', 'args': None},
    'north': {'function': 'move', 'args': ['n']},
    'east': {'function': 'move', 'args': ['e']},
    'south': {'function': 'move', 'args': ['s']},
    'west': {'function': 'move', 'args': ['w']},
    'flee': {'function': 'flee', 'args': None},
}

command_aliases = {
    'q': 'quit',
    'exit': 'quit',
    'c': 'help',
    'commands': 'help',
    'h': 'help',
    'n': 'north',
    'e': 'east',
    's': 'south',
    'w': 'west',
    'f': 'flee',
}

game_map = {
    '0_2': {
        'has_enemy': True,
    }
}

character = {
    'location': [1, 2],
    'hp': 100
}

while True:
    print('L:', character['location'], 'HP:', character['hp'])
    c = read_command()

    globals()[commands[c]['function']](commands[c]['args'])