import os
import pytest
from src.main import parse_log

def test_parse_log(tmp_path, capsys):
    # Create a temporary log file
    log_file = tmp_path / "test.log"
    log_file.write_text("2025-09-03 12:00:01 INFO User login successful\n")

    # Run the parser
    parse_log(str(log_file))

    # Capture printed output
    captured = capsys.readouterr()

    # Check if the log line appears in output
    assert "User login successful" in captured.out
