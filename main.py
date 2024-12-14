from Games import XO
import os

def print_field(class_):
    os.system('clear')
    field = class_.field()
    print(
        f'{field["1"]}|{field["2"]}|{field["3"]}',
        f'{field["4"]}|{field["5"]}|{field["6"]}',
        f'{field["7"]}|{field["8"]}|{field["9"]}',
        sep=f'\n————————\n'
    )

def run(class_):
    data = input("enter an index of a square in the field (from 1 to 9): ")
    class_.make_move(data.strip())
    print_field(class_)

if __name__ == '__main__':
    xo = XO(123)
    xo.del_game()

    xo = XO(123)
    print_field(xo)
    while True:
        run(xo)
        if xo.does_win() or xo.draw():
            xo.del_game()
            break
        