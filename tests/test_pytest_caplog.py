
import logging
import pytest

def divide_numbers(a, b):
    if b == 0:
        logging.error("Cannot divide by zero!")
        return None
    else:
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result

def test_divide_numbers(caplog):
    caplog.set_level(logging.INFO)  # Set the log level to capture INFO messages
    
    result = divide_numbers(10, 2)
    assert result == 5.0
    
    result = divide_numbers(10, 0)
    assert result is None
    
    # Check if the expected log messages are captured
    assert any(record.levelno == logging.ERROR and record.message == "Cannot divide by zero!" for record in caplog.records)
    print('\n')
    assert any(record.levelno == logging.INFO and "Division successful" in record.message for record in caplog.records)
    
    # Print the captured log messages
    print(caplog.text)
