import logging
import sys

def my_function():
    logging.warning("This is a warning message.")
    logging.warning("")  # Empty log message
    logging.warning("Another warning message.")

def test_logging(caplog):
    my_function()

    # Access captured log messages using caplog
    captured_log_messages = [record.message for record in caplog.records if record.message]
    log_output = "\n".join(captured_log_messages)
    print(f"Caplog Output:\n{log_output}")