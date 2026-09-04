import os
import time

if os.name == 'nt':
    os.system('')

RED = '[41m'
WHITE = '[47m'
BLUE = '[44m'
END = '[0m'

def print_flag():
    width = 30
    stripes = [RED, WHITE, BLUE, BLUE, WHITE, RED]
    print('Флаг Таиланда:')
    for color in stripes:
        print(f'{color}{" " * width}{END}')
    print()

def print_pattern(repeats=5):
    print('Узор f:')
    top = '  /\\  ' * repeats
    bottom = ' /  \\ ' * repeats
    print(top)
    print(bottom)
    print()

def plot_function(rows=9, x_start=1, x_end=9):
    xs = list(range(x_start, x_end + 1))
    ys = [1 / x for x in xs]
    y_max, y_min = max(ys), min(ys)

    grid = [[' ' for _ in xs] for _ in range(rows)]
    for col, y in enumerate(ys):
        row = round((y_max - y) / (y_max - y_min) * (rows - 1))
        grid[row][col] = '*'

    print('График функции y = 1/x:')
    for r, line in enumerate(grid):
        y_value = y_max - r * (y_max - y_min) / (rows - 1)
        print(f'{y_value:5.2f} | ' + ' '.join(line))
    print('      +' + '--' * len(xs))
    print('        ' + ' '.join(str(x) for x in xs))
    print()

def read_sequence(path='sequence.txt'):
    numbers = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                numbers.append(float(line))
    return numbers

def print_diagram(numbers):
    positive = [n for n in numbers if n >= 0]
    greater5 = [n for n in positive if n > 5]
    up_to_5 = [n for n in positive if n <= 5]
    total = len(greater5) + len(up_to_5)

    print('Диаграмма процентного соотношения:')
    if total == 0:
        print('Нет данных, удовлетворяющих условию.')
        return

    pct_greater = len(greater5) / total * 100
    pct_up_to_5 = len(up_to_5) / total * 100

    print(f'Числа > 5      : {pct_greater:5.1f}% ' + '#' * round(pct_greater / 2))
    print(f'Числа 0..5     : {pct_up_to_5:5.1f}% ' + '#' * round(pct_up_to_5 / 2))
    print()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_animation():
    frames = [
        '   o   \n  /|\\  \n  / \\  ',
        '   o   \n --|-- \n  / \\  ',
        '   o   \n  |\\   \n  / \\  ',
    ]
    for frame in frames:
        clear_console()
        print(frame)
        time.sleep(0.5)

if __name__ == '__main__':
    print_flag()
    print_pattern()
    plot_function()
    play_animation()