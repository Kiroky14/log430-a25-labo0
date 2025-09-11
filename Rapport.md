# Rapport LAB 0 Kylian
Author : Kylian Pasquereau

## Question 1 :
- Montrer le résultat de l'exécution des tests après qu'un test provoque volontairement une erreur.

```bash
(labo0) PS ~\log430-a25-labo0\src> pytest
=============================================================================================================== test session starts================================================================================================================
platform win32 -- Python 3.13.7, pytest-8.4.2, pluggy-1.6.0
rootdir: ~log430-a25-labo0\src
collected 2 items                                                                                                                                                                                                                                   

tests\test_calculator.py F.                                                                                                                                                                                                                   [100%]

===================================================================================================================== FAILURES===================================================================================================================== 
_____________________________________________________________________________________________________________________ test_app _____________________________________________________________________________________________________________________ 

    def test_app():
        my_calculator = Calculator()
>       assert my_calculator.get_hello_message() == "== Calculatrice v1.0"
E       AssertionError: assert '== Calculatrice v1.0 ==' == '== Calculatrice v1.0'
E
E         - == Calculatrice v1.0
E         + == Calculatrice v1.0 ==
E         ?                     +++

tests\test_calculator.py:14: AssertionError
============================================================================================================= short test summary info============================================================================================================== 
FAILED tests/test_calculator.py::test_app - AssertionError: assert '== Calculatrice v1.0 ==' == '== Calculatrice v1.0'
=========================================================================================================== 1 failed, 1 passed in 0.18s============================================================================================================
