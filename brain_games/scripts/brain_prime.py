#!/usr/bin/env python3

from brain_games.game_engine import play_game
from brain_games.games import brain_prime_logic


def main():
    play_game(brain_prime_logic)


if __name__ == '__main__':
    main()
