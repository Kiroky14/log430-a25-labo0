"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="


def test_addition():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 5
    assert my_calculator.addition(-1, 1) == 0
    assert my_calculator.addition(-1, -1) == -2

def test_subtraction():
    my_calculator = Calculator()
    assert my_calculator.subtraction(5, 3) == 2
    assert my_calculator.subtraction(2, 3) == -1
    assert my_calculator.subtraction(-1, -1) == 0

def test_multiplication():
    my_calculator = Calculator()
    assert my_calculator.multiplication(4, 3) == 12
    assert my_calculator.multiplication(4, 0) == 0
    assert my_calculator.multiplication(-2, 3) == -6

def test_division():
    my_calculator = Calculator()
    assert my_calculator.division(10, 2) == 5
    assert my_calculator.division(10, 0) == "Erreur : division par zéro"
    assert my_calculator.division(-6, 2) == -3
