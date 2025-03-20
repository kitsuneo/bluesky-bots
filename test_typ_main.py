from datetime import date

import pytest
from typ import generate_posting_string, generate_log_string


class TestStringClass:
    def test_posting_string(self):
        test_string = generate_posting_string()
        assert type(test_string) is str
        assert len(test_string) > 0
        assert '\U0001F7E6' in test_string or '\U00002B1C' in test_string

    def test_logging_string(self):
        test_string = generate_log_string(True)
        assert type(test_string) is str
        assert len(test_string) > 0
        assert test_string.startswith(str(date.today()))

        test_string_f = generate_log_string(False)
        assert test_string_f.startswith(str(date.today()))
