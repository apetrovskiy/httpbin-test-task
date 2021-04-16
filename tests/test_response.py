import pytest
from typing import Any
from src.main.constants import TOKEN
from src.main.endpoint_reader import get_response


test_data = [
    (None, 401),
    ("Bearer abc", 403),
    (TOKEN, 200)
]


@pytest.mark.parametrize("token,expected_result", test_data)
def test_response(token: Any, expected_result: int):
    assert expected_result == get_response(token).status_code
