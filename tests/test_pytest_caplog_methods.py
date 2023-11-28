import logging

def function_that_logs():
    logging.info("Starting process")
    logging.warning("An issue occurred")
    logging.info("Ending process")

def test_function_logs_caplog_messages(caplog):
    """Testing the caplog.messages attribute"""
    caplog.set_level(logging.INFO)  # Set the caplog level to INFO and above
    function_that_logs()
    assert caplog.messages == ["Starting process", "An issue occurred", "Ending process"]

def test_function_logs_caplog_text(caplog):
    """Testing the caplog.text attribute"""
    caplog.set_level(logging.INFO)  # Set the caplog level to INFO and above
    function_that_logs()
    assert "Starting process" in caplog.text
    assert "An issue occurred" in caplog.text
    assert "Ending process" in caplog.text

def test_function_logs_caplog_record_tuples(caplog):
    """Testing the caplog.record_tuples attribute"""
    caplog.set_level(logging.INFO)  # Set the caplog level to INFO and above
    function_that_logs()
    assert caplog.record_tuples == [
        ("root", logging.INFO, "Starting process"),
        ("root", logging.WARNING, "An issue occurred"),
        ("root", logging.INFO, "Ending process"),
    ]

def test_function_logs_caplog_records(caplog):
    """Testing the caplog.records attribute"""
    caplog.set_level(logging.INFO)  # Set the caplog level to INFO and above
    function_that_logs()
    assert len(caplog.records) == 3
    assert caplog.records[0].message == "Starting process"
    assert caplog.records[1].message == "An issue occurred"
    assert caplog.records[2].message == "Ending process"

def test_function_logs_caplog_clear(caplog):
    """Testing the caplog.clear() method"""
    caplog.set_level(logging.INFO)  # Set the caplog level to INFO and above
    function_that_logs()
    assert len(caplog.records) == 3
    caplog.clear()
    assert len(caplog.records) == 0