from unittest.mock import patch
import unittest
import pytest
from project import create,load


def test_create():
    assert create("week") == "week.csv"
    assert create("2023 Todo list") == "2023 Todo list.csv"

def test_create():
    assert load("week.csv") == "week.csv"
    assert load("july goals.csv") == "july goals.csv"
