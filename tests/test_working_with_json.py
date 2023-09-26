import pytest
from src.utils.working_with_json import load_json, select_executed_operation, sort_descending

PATH = './src/data/operations.json'


@pytest.fixture
def operations():
    operations = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-06-26T10:50:58.294041",
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
        },
        {
            "id": 41428829,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },

    ]

    return operations


def test_load_json():
    """
    Проверяет работу функции load_json
    """
    print(PATH)
    assert type(load_json(PATH)) == type([])


def test_select_executed_operation(operations):
    condition = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-06-26T10:50:58.294041",
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
    ]

    assert select_executed_operation(operations) == condition
    assert select_executed_operation([]) == []


def test_sort_descending(operations):
    condition = [
        {
            "id": 41428829,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-06-26T10:50:58.294041",
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
        },

    ]

    assert sort_descending(operations) == condition
    assert sort_descending([]) == []
