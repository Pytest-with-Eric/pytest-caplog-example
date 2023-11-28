import logging

def greet(name):
    logging.info(f"Hello, {name}!")

def test_greet_logs_correct_message(caplog):
    caplog.set_level(logging.INFO)
    greet("Alice")
    assert "Hello, Alice!" in caplog.text
