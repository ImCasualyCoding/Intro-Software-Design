
import pytest
from glob_lit import Lit
from glob_one_or_more import OneOrMore

def test_one_or_more_empty():
    pattern = OneOrMore()
    assert pattern.match("") is True

def test_one_or_more_matches_entire_string():
    pattern = OneOrMore()
    assert pattern.match("abc") is True

def test_one_or_more_matches_as_prefix():
    pattern = OneOrMore(Lit("def"))
    assert pattern.match("abcdef") is True

def test_one_or_more_matches_as_suffix():
    pattern = Lit("abc", OneOrMore())
    assert pattern.match("abcdef") is True

def test_one_or_more_matches_interior():
    pattern = Lit("a", OneOrMore(Lit("c")))
    assert pattern.match("abc") is True