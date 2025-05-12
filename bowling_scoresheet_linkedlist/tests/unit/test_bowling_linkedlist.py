import pytest
from bowling_linkedlist import Game



######## get_score ###########

def test_get_score_frame_1_to_9_normal_score():
    game = Game()
    roll1, roll2, roll3 = '2','7',""
    frame_count = 1
    
    assert game.get_score(frame_count, roll1, roll2, roll3) == 9

def test_get_score_frame_1_to_9_spare():
    game = Game()
    roll1, roll2, roll3 = '2','/',""
    frame_count = 2
    
    assert game.get_score(frame_count, roll1, roll2, roll3) == 10

def test_get_score_frame_1_to_9_strike():
    game = Game()
    roll1, roll2, roll3 = 'X','""',""
    frame_count = 3
    
    assert game.get_score(frame_count, roll1, roll2, roll3) == 10

def test_get_score_tenth_frame_normal_score():
    game = Game()
    frame_count = 10
    roll1, roll2, roll3 = '2','6',""
    
    assert game.get_score(frame_count, roll1, roll2, roll3) == 8

def test_get_score_tenth_frame_spare():
    game = Game()
    frame_count = 10
    roll1, roll2, roll3 = '2','/','3'
    
    assert game.get_score(frame_count, roll1, roll2, roll3) == 13

def test_get_score_tenth_frame_strike():
    game = Game()
    roll1, roll2, roll3 = 'X','X','X'
    frame_count = 10
    
    assert game.get_score(frame_count, roll1, roll2, roll3) == 30

def test_get_score_tenth_frame_spare_strike():
    game = Game()
    roll1, roll2, roll3 = '1','/','X'
    frame_count = 10
    
    assert game.get_score(frame_count, roll1, roll2, roll3) == 20


######## calculate_score ###########

def test_calculate_score_all_zeros():
    game = Game()
    game.load_scores('00 00 00 00 00 00 00 00 00 00')
    game.calculate_score()

    scores = []
    current = game.head
    while current:
        scores.append(current.score)
        current = current.next

    assert scores == [0]*10 
    assert sum(scores) == 0

def test_calculate_score_all_spares():
    game = Game()
    game.load_scores('1/ 2/ 3/ 4/ 5/ 6/ 7/ 8/ 9/ 9/9')
    game.calculate_score()

    scores = []
    current = game.head
    while current:
        scores.append(current.score)
        current = current.next

    assert scores == [12,13,14,15,16,17,18,19,19,19]
    assert sum(scores) == 162

def test_calculate_score_all_strikes():
    game = Game()
    game.load_scores('X X X X X X X X X XXX')
    game.calculate_score()

    scores = []
    current = game.head
    while current:
        scores.append(current.score)
        current = current.next

    assert scores == [30]*10
    assert sum(scores) == 300

def test_calculate_score_mixed_1():
    game = Game()
    game.load_scores('X 7/ 81 7/ 50 06 X X 80 XXX')
    game.calculate_score()

    scores = []
    current = game.head
    while current:
        scores.append(current.score)
        current = current.next

    assert scores == [20, 18, 9, 15, 5, 6, 28, 18, 8, 30]
    assert sum(scores) == 157

def test_calculate_score_mixed_2():
    game = Game()
    game.load_scores('81 09 2/ X 63 70 52 X 06 2/X')
    game.calculate_score()

    scores = []
    current = game.head
    while current:
        scores.append(current.score)
        current = current.next

    assert scores == [9, 9, 20, 19, 9, 7, 7, 16, 6, 20]
    assert sum(scores) == 122

def test_calculate_score_mixed_3():
    game = Game()
    game.load_scores('62 72 34 8/ 90 X X X 63 8/7')
    game.calculate_score()

    scores = []
    current = game.head
    while current:
        scores.append(current.score)
        current = current.next

    assert scores == [8, 9, 7, 19, 9, 30, 26, 19, 9, 17]
    assert sum(scores) == 153

def test_calculate_score_mixed_4():
    game = Game()
    game.load_scores('X X 9/ 8/ 80 8/ 9/ X 9/ 9/5')
    game.calculate_score()

    scores = []
    current = game.head
    while current:
        scores.append(current.score)
        current = current.next

    assert scores == [29, 20, 18, 18, 8, 19, 20, 20, 19, 15]
    assert sum(scores) == 186

def test_calculate_score_all_open_frames():
    game = Game()
    game.load_scores('12 06 45 22 35 80 90 20 51 62')
    game.calculate_score()

    scores = []
    current = game.head
    while current:
        scores.append(current.score)
        current = current.next

    assert scores == [3, 6, 9, 4, 8, 8, 9, 2, 6, 8]
    assert sum(scores) == 63
    
def test_calculate_score_single_strike_middle():
    game = Game()
    game.load_scores('00 00 X 43 00 00 00 00 00 00')
    game.calculate_score()

    scores = []
    current = game.head
    while current:
        scores.append(current.score)
        current = current.next

    assert scores == [0, 0, 17, 7, 0, 0, 0, 0, 0, 0]
    assert sum(scores) == 24

def test_calculate_score_double_strike_followed_by_3():
    game = Game()
    game.load_scores('00 00 X X 30 00 00 00 00 00')
    game.calculate_score()

    scores = []
    current = game.head
    while current:
        scores.append(current.score)
        current = current.next

    assert scores == [0, 0, 23, 13, 3, 0, 0, 0, 0, 0]
    assert sum(scores) == 39

def test_calculate_score_double_strike_followed_by_3():
    game = Game()
    game.load_scores('00 00 X X 30 00 00 00 00 00')
    game.calculate_score()

    scores = []
    current = game.head
    while current:
        scores.append(current.score)
        current = current.next

    assert scores == [0, 0, 23, 13, 3, 0, 0, 0, 0, 0]
    assert sum(scores) == 39


######## score_tenth_frame ###########

def test_score_tenth_frame_triple_strike():
    game = Game()
    
    tenth_frame_score = game.score_tenth_frame('X', 'X', 'X')
    assert tenth_frame_score == 30

def test_score_tenth_frame_double_strike():
    game = Game()
    
    tenth_frame_score = game.score_tenth_frame('X', 'X', '0')
    assert tenth_frame_score == 20

def test_score_tenth_frame_single_strike():
    game = Game()
    
    tenth_frame_score = game.score_tenth_frame('X', '0', '')
    assert tenth_frame_score == 10

def test_score_tenth_frame_spare():
    game = Game()
    tenth_frame_score = game.score_tenth_frame('2', '/', '0')
    assert tenth_frame_score == 10














