
import logging
import sys

def greet(name):
    print(f"Hello, {name}!")

def test_greet(capsys):
    greet("Alice")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Alice!\n"