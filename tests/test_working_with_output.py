import pytest
from src.utils.working_with_output import (get_date_representation, get_bankcard_num_representation,
                                           get_bank_account_num_representation, is_bank_account,
                                           get_sum_operation, get_operation_representation)


@pytest.fixture()
def operation():
    operation = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
    return operation


def test_get_date_representation():
    assert get_date_representation('2019-08-26T10:50:58.294041') == '26.08.2019'
    assert get_date_representation('') == ''


def test_get_bankcard_num_representation():
    assert get_bankcard_num_representation('Maestro 1596837868705199') == "Maestro 1596 83** **** 5199"
    assert get_bankcard_num_representation(None) == ''


def test_get_bank_account_num_representation():
    assert get_bank_account_num_representation('Счет 64686473678894779589') == 'Счет **9589'
    assert get_bank_account_num_representation(None) == ''


def test_is_bank_account():
    assert is_bank_account('Счет 64686473678894779589') is True
    assert is_bank_account('Maestro 1596837868705199') is False
    assert is_bank_account('') is False


def test_get_sum_operation(operation):
    assert get_sum_operation(operation['operationAmount']) == "31957.58 руб."


def test_get_operation_representation(operation):
    condition = ('26.08.2019 Перевод организации\n'
                 + 'Maestro 1596 83** **** 5199 -> Счет **9589\n'
                 + '31957.58 руб.')

    assert get_operation_representation(operation) == condition
