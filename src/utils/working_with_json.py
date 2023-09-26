from json import loads
from datetime import datetime


def load_json(path: str):
    """
    Читает файл с данными в формате json
    и дессерилизует данные json
    :param path: путь данным файла в формате json
    :return: дессериализованную струкутуру
    """
    with open(path, encoding='utf8') as file:
        return [operation for operation in loads(file.read()) if operation != {}]


def select_executed_operation(operations):
    """
    Возвразащает list выполненных банковских операций
    :param operations: list банковских операций
    :return: list выполенных операций
    """
    return [operation for operation in operations if operation["state"] == 'EXECUTED']


def sort_descending(operations):
    """
    Сортивка банковских операций по убыванию
    :param operations: list банковских операций
    :return: list отсортированный по убыванию  банковсих операций
    """
    sort_operations = sorted(
        operations,
        key=lambda operation: datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f'),
        reverse=True
    )
    return sort_operations
