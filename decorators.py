from datetime import datetime
import time


def logger(old_function):

    def new_function(*args, **kwargs):
        time_function = datetime.now()
        result = old_function(*args, **kwargs)

        line = '\n' + str(time_function) + ' Функция: ' + old_function.__name__ + '\n' + 'Аргументы: ' + str([args, kwargs]) \
               + '\n' + ' Результат: ' + str(result)
        with open('logger.txt', 'a+') as file:
            file.writelines(line)
        return result

    return new_function


documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

@logger
def main():
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            @logger
            def doc_people(documents):
                input_doc = input('Введите номер документа: ')
                for docs in documents:
                    if docs['number'] == input_doc:
                        return docs['name']
            print(doc_people(documents))
        elif user_input == 's':
            @logger
            def docs_shelf(documents):
                input_doc_number = input('Введите номер документа: ')
                for shelf, number in directories.items():
                    if input_doc_number in number:
                        return f'Документ находится на {shelf} полке'
            print(docs_shelf(documents))
        elif user_input == 'l':
            @logger
            def doc_list(documents):
                for docs in documents:
                    print(f'{docs["type"]} {docs["number"]} {docs["name"]}')
            doc_list(documents)
        elif user_input == 'a':
            @logger
            def doc_add(documents):
                input_add_type = input('Введите тип документа: ')
                input_add_number = input('Введите номер документа: ')
                input_add_name = input('Введите имя и фамилию владельца документа: ')
                input_add_shelf = input('Введите номер полки, на которую необходимо положить новый документ: ')
                documents.append({'type': input_add_type, 'number': input_add_number, 'name': input_add_name})
                directories.update({input_add_shelf: input_add_number})
                print(f'Документ с типом {input_add_type} и номером {input_add_number} '
                      f'добавили на полку с номером {input_add_shelf}')
            print(doc_add(documents))
            print(documents)
            print(directories)
        elif user_input == 'q':
            print('GoodBye!')
            break


main()
