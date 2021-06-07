import threading

from constants import *
from drawer import *
from events import *
from state import State


def main():
    screen = draw_init()
    state = State()
    clock = pygame.time.Clock()

    while True:
        event_handler(screen, state)
        draw_all(screen, clock, state)
        clock.tick(FPS)


if __name__ == '__main__':
    main()
