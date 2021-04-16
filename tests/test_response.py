import pytest
from typing import Any
from src.main.constants import TOKEN
from src.main.endpoint_reader import get_response


test_data_for_working_cases = [
    (None, 401),
    (TOKEN, 200)
]


@pytest.mark.parametrize("token,expected_result", test_data_for_working_cases)
def test_expected_response(token: Any, expected_result: int):
    assert expected_result == get_response(token).status_code


test_data_for_wrong_cases = [
    ("Bearer abc", 403)
]


# @pytest.mark.skip("TODO: endpoint returns 200 on sending invalid token \
#     while it should return 403")
@pytest.mark.parametrize("token,expected_result", test_data_for_wrong_cases)
def test_inexplicable_response(token: Any, expected_result: int):
    assert expected_result == get_response(token).status_code
