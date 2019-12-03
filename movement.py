def user_choice():
    c = ''
    while c not in ['p', 'v']:
        c = input('(p)arem või (v)asak? ')
    return c

again = 'j'
while again == 'j':
    choice = user_choice()
    if choice == 'v':
        print('hea valik!')
    elif choice == 'p':
        print('kohtusid karuga :(')
    
    again = input('kas veel (j/e)? ')
    while again not in ['j', 'e']:
        again = input('kas veel (j/e)? ')