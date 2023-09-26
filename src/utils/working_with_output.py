
def get_date_representation(str_data):
    """
    Создает представление в формате "ДД.ММ.ГГГГ" (пример: 14.10.2018).
    :param: дата в формате строки "2019-08-26T10:50:58.294041"
    :return: дату в форме строки "ДД.ММ.ГГГГ"
    """
    date_format = str_data[:10].split('-')
    if len(date_format) != 3:
        return ""
    else:
        return f'{date_format[2]}.{date_format[1]}.{date_format[0]}'


def get_bankcard_num_representation(bankcard):
    """
    Создает представление банковского номера карты в формате "XXXX XX** **** XXXX"
    :param bankcard_num: номер карты в формате "Maestro 1596837868705199"
    :return: строку банковского номера карты в формате "XXXX XX** **** XXXX"
    """
    if bankcard is None:
        return ''

    bankcard_lst = bankcard.split(' ')
    bankcard_payment_system = bankcard_lst[0]
    bankcard_num = bankcard_lst[1]

    representation = f'{bankcard_payment_system} {bankcard_num[:4]} {bankcard_num[4:6]}** **** {bankcard_num[-4:]}'

    return representation


def get_bank_account_num_representation(bank_account_num):
    """
    Создает представление номера счета в формате "**XXXX"
    :param bank_account_num: номера счета в формате "Счет 64686473678894779589"
    :return: строку редставление номера счета в формате "**XXXX"
    """
    if bank_account_num is None:
        return ''
    else:
        return f'Счет **{bank_account_num[-4:]}'


def is_bank_account(from_str):
    """
    Проверяет является ли строка счтетом
    :param from_str: строка занчение from/to
    :return: bool
    """
    return from_str[:4] == 'Счет'


def get_sum_operation(operation_amount):
    """
    Возвращает представления суммы перевода
    :param operation_amount: словать  operationAmount
    :return: строка формата <сумма перевода> <валюта>
    """
    sum_operation = f"{operation_amount['amount']} {operation_amount['currency']['name']}"
    return sum_operation


def get_operation_representation(operation: dict):
    """
    Созсдает представление операции
    :param operation: структура операция
    :return: строка предствления операции
    """
    transfer_date = get_date_representation(operation['date'])
    description = operation['description']

    # Получения представления откуда был сделан перевод
    # используется метод get так как этого значения может и не быть в словаре
    operation_from = operation.get('from')
    if operation_from is None:
        # если значения нет то представление пустая строка
        from_transfer = ''
    elif is_bank_account(operation_from):
        # если это счет тогда получаем представление счета
        from_transfer = get_bank_account_num_representation(operation_from)
    else:
        # иначе пполучаем представление банковской карты
        from_transfer = get_bankcard_num_representation(operation_from)

    # Получения представления куда был сделан перевод
    if is_bank_account(operation['to']):
        # если это счет тогда получаем представление счета
        to_transfer = get_bank_account_num_representation(operation['to'])
    else:
        # иначе пполучаем представление банковской карты
        to_transfer = get_bankcard_num_representation(operation['to'])

    # получаем представление суммы
    sum_operation = get_sum_operation(operation['operationAmount'])

    operation_format = (f'{transfer_date} {description}\n'
                        + f'{from_transfer} -> {to_transfer}\n'
                        + f'{sum_operation}')

    return operation_format
