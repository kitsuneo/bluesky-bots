from datetime import date

import pytest
from main import generate_posting_string, generate_log_string


class TestClass:
    def test_posting_string(self):

        test_string = generate_posting_string()
        assert type(test_string) == str
        assert len(test_string) > 0
        assert '\u2591' in test_string or '\u2588' in test_string

    def test_logging_string(self):
        test_string = generate_log_string(True)
        assert type(test_string) == str
        assert len(test_string) > 0
        assert str(date.today()) in test_string