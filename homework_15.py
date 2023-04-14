import argparse
import logging

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level=logging.INFO, filename='my_func.log', encoding='utf-8',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)



def get_number(num: int, mod: int = 10) -> str:
    """
    Функция получает на вход целое число, систему исчисления и возвращает его  строковое представление.
    : number: само число
    : mod: система исчисления
    : return: строковое представление
    """
    result = ''
    if mod < 0:
        logger.error(f'Система исчисления {mod} не существует')
        return float('inf')
    while num != 0:
        try:
            result = str(num % mod) + result
            num //= mod
         except ZeroDivisionError as e:
            logger.error(f'Система исчисления {mod} не существует')
            return float('inf')
    logger.info(f'{num}, {mod} = {result}')
    return result

def parser_func():
    parser = argparse.ArgumentParser(description='Аргументы из строки')
    parser.add_argument('--num')
    parser.add_argument('--mod', default=10)
    args = parser.parse_args()
    print(args)
    return get_number(int(args.num), int(args.mod))


if __name__ == '__main__':
    print(get_number(57, 2))
    print(get_number(57, 0))
    print(get_number(57, -2))
    parser_func()
        
