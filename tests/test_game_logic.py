import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logic_utils import check_guess, parse_guess, update_score

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_parse_valid_input():
    ok, value, err = parse_guess("25")
    assert ok is True
    assert value == 25
    assert err is None


def test_parse_invalid_input():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None


def test_parse_empty_input():
    ok, value, err = parse_guess("")
    assert ok is False


def test_score_win_decreases_with_attempts():
    score1 = update_score(0, "Win", 1)
    score2 = update_score(0, "Win", 5)
    assert score1 > score2


def test_score_penalty():
    score = update_score(100, "Too High", 2)
    assert score == 95