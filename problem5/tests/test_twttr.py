from twttr import shorten
import pytest

def test_upper_vowel():
    assert shorten("Assert") == "ssrt"

def test_lower_vowel():
    assert shorten("Test") == "Tst"

def test_number():
    assert shorten("CS50") == "CS50"

def test_punctuation():
    assert shorten("?") == "?"
