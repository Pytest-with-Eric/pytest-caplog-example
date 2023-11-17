
import logging

def my_function():
    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")

def test_logging_levels(caplog):
    caplog.set_level(logging.DEBUG)  # Set the log level to capture all levels
    
    my_function()
    
    # Print the captured log messages
    print(caplog.text)