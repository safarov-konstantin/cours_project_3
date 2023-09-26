import src.utils.working_with_output as working_output
import src.utils.working_with_json as working_json

PATH = './data/operations.json'


def main():
    # читаем файл дынных с операциями
    operations_all = working_json.load_json(PATH)

    # получеме только выполененые операции
    operations_select = working_json.select_executed_operation(operations_all)

    # сортируем выполенные операции по убыванию
    operations_sort = working_json.sort_descending(operations_select)

    # получаем пять последних операций
    operations_last_five = operations_sort[:5]

    # запускаем основной цикл
    for operation in operations_last_five:
        # получаем форматированную строку операции
        representation_operation = working_output.get_operation_representation(operation)

        # выводим строку в консоль
        print(representation_operation)

        # отступ в консоли
        print()


if __name__ == '__main__':
    main()
