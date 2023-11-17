
import logging
import sys

def my_function():
    print("This is a print statement.")
    logging.warning("This is a warning message.")

def test_logging(capsys, caplog):
    my_function()

    # Access captured stdout using capsys
    captured_stdout = capsys.readouterr().out
    print(f"\nCapsys Output:\n{captured_stdout}\n")

    # Access captured log messages using caplog
    print(f"Caplog Output:\n{caplog.text}")
