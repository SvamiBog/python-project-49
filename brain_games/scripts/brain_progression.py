#!/usr/bin/env python3

from brain_games.game_engine import play
from brain_games.games import brain_progression_logic


def main():
    play(brain_progression_logic)


if __name__ == '__main__':
    main()
