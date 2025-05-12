import pytest
from bowling_linkedlist import Game


""" functional tests to test system behaviour of bowling_linkedlist.py  """


###### get_running_total #######

def test_perfect_game():
    game = Game()
    game.load_scores('X X X X X X X X X XXX')
    game.calculate_score()
    total_in_list = game.get_running_total()
    assert total_in_list == [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]


def test_game_of_spares_with_5():
    game = Game()
    game.load_scores('5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5')
    game.calculate_score()
    total_in_list = game.get_running_total()
    assert total_in_list == [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]


###### validate integration of multiple methods: load_scores(), calculate_score(), and print_frames(). #######

def test_print_frames_perfect_game():
    game = Game()
    game.load_scores('X X X X X X X X X XXX')
    game.calculate_score()

    expected = "-".join([
        '[Frame 1: <X> <> Score: 30]',
        '[Frame 2: <X> <> Score: 60]',
        '[Frame 3: <X> <> Score: 90]',
        '[Frame 4: <X> <> Score: 120]',
        '[Frame 5: <X> <> Score: 150]',
        '[Frame 6: <X> <> Score: 180]',
        '[Frame 7: <X> <> Score: 210]',
        '[Frame 8: <X> <> Score: 240]',
        '[Frame 9: <X> <> Score: 270]',
        '[Frame 10: <X> <X> <X> Score: 300]',
    ])
    assert game.print_frames() == expected


















