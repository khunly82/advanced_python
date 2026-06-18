import asyncio
import curses
from collections import deque
from random import randint

async def main(screen: curses.window):
    SIZE = 15
    snake = deque()
    snake.append((0,0))
    snake.append((0,1))
    snake.append((0,2))
    snake.append((0,3))
    snake.append((0,4))
    food = None

    def random_food():
        nonlocal food
        food = (randint(0, SIZE - 1), randint(0, SIZE - 1))
        if food in snake:
            random_food()
        else:
            screen.addstr(food[1] + 1, food[0] + 1, '0')
    
    random_food()


    def print_area():
        screen.addstr(0, 0, f'╔{'═' * (SIZE)}╗')
        for i in range(1, SIZE + 1):
            screen.addstr(i, 0, f'║{' ' * (SIZE)}║')
        screen.addstr(SIZE + 1, 0, f'╚{'═' * (SIZE)}╝')

    screen.clear()
    curses.curs_set(False)
    print_area()
    screen.refresh()

    for item in snake:
        screen.addstr(item[1] + 1, item[0] + 1, 'X')
    screen.addstr(food[1] + 1, food[0] + 1, '0')
    
    screen.refresh()

    direction = 1 # 1 North 2 Est 3 South 4 West

    async def move():
        nonlocal snake, direction, food
        while True:
            await asyncio.sleep(0.2)
            head = snake[-1]
            tail = snake.popleft()
            screen.addstr(tail[1] + 1, tail[0] + 1, ' ')
            if direction == 0: snake.append((head[0], (head[1] - 1 + SIZE) % SIZE )) 
            if direction == 1: snake.append(((head[0] + 1) % SIZE , head[1]))
            if direction == 2: snake.append((head[0], (head[1] + 1) % SIZE))
            if direction == 3: snake.append(((head[0] - 1 + SIZE) % SIZE, head[1]))
            head = snake[-1]
            screen.addstr(head[1] + 1, head[0] + 1, 'X')

            if head == food:
                snake.appendleft(tail)
                screen.addstr(tail[1] + 1, tail[0] + 1, 'X')
                random_food()

            if head in list(snake)[:-1]:
                screen.addstr(0, 0, 'GAME OVER')
                screen.refresh()
                break
            screen.refresh()

    def get_direction():
        nonlocal direction
        while True:
            key = screen.getch()
            if key == curses.KEY_UP: direction = 0
            if key == curses.KEY_DOWN: direction = 2
            if key == curses.KEY_LEFT: direction = 3
            if key == curses.KEY_RIGHT: direction = 1
            if key == 27:
                break


    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, get_direction)

    await move()

    loop.close()

curses.wrapper(lambda screen: asyncio.run(main(screen)))