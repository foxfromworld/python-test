from countOdds import *

def test_evenL_evenH():
    assert countOdds(4,8) == 2

def test_oddL_evenH():
    assert countOdds(3,8) == 2

def test_evenL_oddH():
    assert countOdds(4,7) == 3

def test_oddL_oddH():
    assert countOdds(3,7) == 0
