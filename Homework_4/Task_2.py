from typing import Union

string_parameter: str = 'Пример'
number_parameter: int = 10
list_parameter: list[int] = [1, 2, 3]

# Функция создания обратного словаря 
# (ключ - значение переданного аргумента, а значение — имя аргумента)
def create_reverse_dictionary(**kwargs: Union[int, float, str]) -> dict[Union[int, float, str], str]:
    result: dict[Union[int, float, str], str] = {}
    for key, value in kwargs.items():
        if isinstance(key, (int, float, str)):
            result[value] = key
        else:
            result[str(value)] = key
    return result

def __main() -> None:
    string_parameter: str = 'Пример'
    number_parameter: int = 10
    list_parameter: list[int] = [1, 2, 3]

    arguments_dict = create_reverse_dictionary(string_parameter=string_parameter, 
                                               number_parameter=number_parameter, 
                                               list_parameter=str(list_parameter))
    print(arguments_dict)
    
if __name__ == '__main__':
    __main()