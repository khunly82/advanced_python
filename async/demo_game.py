import asyncio
import curses

async def main(screen: curses.window):
    screen.clear()
    curses.curs_set(False)
    screen.addstr(0, 0, 'X')
    screen.refresh()

    x, y = 0, 0
    direction = 1 # 1 North 2 Est 3 South 4 West

    async def move():
        nonlocal x, y, direction
        while True:
            await asyncio.sleep(1)
            screen.addstr(y, x, ' ')
            if direction == 0: y -= 1
            if direction == 1: x += 1
            if direction == 2: y += 1
            if direction == 3: x -= 1
            screen.addstr(y, x, 'X')
            screen.refresh()

    def get_direction():
        nonlocal direction
        while True:
            key = screen.getkey()
            if key == 'KEY_UP': direction = 0
            if key == 'KEY_DOWN': direction = 2
            if key == 'KEY_LEFT': direction = 3
            if key == 'KEY_RIGHT': direction = 1


    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, get_direction)

    await move()



curses.wrapper(lambda screen: asyncio.run(main(screen)))