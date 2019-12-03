char_location = [1, 2]

game_map = {
    '2_1': {
        'has_enemy': True
    }
}

while True:
    char_location_str = '_'.join([str(el) for el in char_location])
    if char_location_str in game_map:
        if 'has_enemy' in game_map[char_location_str]:
            print('Enemy!!!')
    else:
        print(char_location_str)

    move = ''
    while move not in ['n', 'e', 's', 'w']:
        move = input('n/e/s/w: ')
        if move == 'n' and char_location[0] != 0:
            char_location[0] -= 1
        elif move == 's' and char_location[0] != 3:
            char_location[0] += 1
        elif move == 'w' and char_location[1] != 0:
            char_location[1] -= 1
        elif move == 'e' and char_location[1] != 3:
            char_location[1] += 1
