from __future__ import annotations

from src.constants import all_operands
from src.errrors import ExtraneousError, EmptyError, JointOperandsError, BadInputError, BadDigit, NotDigitError
from typing import Union

def multiplyy(n: list[str], stek: list[str], i: int) -> tuple[list[str], list[str]]:
    if n[i + 1] == '-':
        stek.append(float(float(stek[-1]) * float(n[i + 2]) * -1))
        stek.pop(-2)
        n.pop(i + 1)
        n.pop(i + 1)
    else:
        stek.append(float(float(stek[-1]) * float(n[i + 1])))
        stek.pop(-2)
        n.pop(i + 1)


    return stek, n


def divisionn(n: list[str], stek: list[str], i: int) -> tuple[list[str], list[str]]:
    if error_0(n, i) == False:
        return 'zero'

    if n[i + 1] == '-':
        stek.append(float(stek[-1]) / float(n[i + 2]) * -1)
        stek.pop(-2)
        n.pop(i + 1)
        n.pop(i + 1)

    else:
        stek.append(float(stek[-1]) / float(n[i + 1]))
        stek.pop(-2)
        n.pop(i + 1)

    return stek, n


def procent(n: list[str], stek: list[str], i: int) ->  str | tuple[list[str], list[str]]:
    if error_0(n, i) == False:
        return 'zero'

    if error_bad_digit(stek[-1]) == False:
        return 'not int'

    if n[i + 1] == '-':
        stek.append(float(int(stek[-1]) % (-1 * int(n[i + 2]))))
        stek.pop(-2)
        n.pop(i + 1)
        n.pop(i + 1)

    else:
        stek.append(float(stek[-1]) % int(n[i + 1]))
        stek.pop(-2)
        n.pop(i + 1)

    return stek, n


def integer_division(n: list[str], stek: list[str], i: int) -> str |  tuple[list[str], list[str]]:
    if error_0(n, i) == False:
        return 'zero'

    if error_bad_digit(stek[-1]) == False:
        return 'not int'

    if n[i + 1] == '-':
        stek.append(float(int(stek[-1]) // int(n[i + 2]) * -1))
        stek.pop(-2)
        n.pop(i + 1)
        n.pop(i + 1)

    else:
        stek.append(float(int(stek[-1])) // int(n[i + 1]))
        stek.pop(-2)
        n.pop(i + 1)

    return stek, n


def is_float(s: str) -> bool:
    """
    функция проверяет является ли строка float
    :param digit: строка, которую нужно проверить
    :return:  либо 1 (да), либо 0 (нет)
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


def error_extraneous(n: str) -> bool:
    """
    функция проверяет строку на посторонние символы
    :param n: входная строка
    :return: либо True (ошибка), либо False (который означает, что все ок)
    """
    for i in n:
        if not (i.isnumeric()) and i not in (all_operands or ' .'):
            return True

    return False


def error_empty_input(n: str) -> bool:
    """
    функция проверяет пустоту ввода
    :param n: входная строка n
    :return: либо True (ошибка), либо False (который означает, что все ок)
    """
    return not n.strip()


def edit(n: str) -> str:
    """
    функция преобразовывает n: выделяет операнды пробелами, убирает лишние пробелы, заменяет все ',' на '.'
    :param n: входная строка
    :return: отредактированная строка
    """
    n = n.replace('+', ' + ')
    n = n.replace('-', ' - ')
    n = n.replace('*', ' * ')
    n = n.replace('/', ' / ')
    n = n.replace('%', ' % ')
    n = n.replace(',', '.')
    n = n.replace('  ', ' ')

    n.lstrip()

    return n


def error_joint_operands(n: str) -> bool:
    """
    функция проверяет на наличие стыка операндов в строке
    :param n: отредактированная строка n
    :return: либо True (ошибка), либо False (который означает, что все ок)
    """
    if '- *' in n or '- /' in n or '- %' in n or '- #' in n or '+ *' in n or '+ /' in n or '+ %' in n or '+ #' in n or '* *' in n or '# #' in n or '% %' in n or '% /' in n or '% *' in n or '% #' in n or '/ *' in n or '/ #' in n or '/ %' in n or '* /' in n or '* %' in n or '* #' in n or '# *' in n or '# /' in n or '# %' in n:
        return 1

    if n[0:3] == '- -' or n[0:3] == '+ +' or n[0:3] == '+ -' or n[0:3] == '- +':
        return True

    k: int = 0
    for i in n:
        if k == 3:
            return True
        if (is_float(i)):
            k = 0
        elif i != ' ':
            k += 1

    return False


def edit_2(n: str) -> str:
    """
    функция заменяет // на #, убирает унарные знаки, преобразовывает строку n в массив и убирает из него элементы = ''
    :param n: отредактированная функция n
    :return: массив n
    """
    n = n.replace('+ -', '-')
    n = n.replace('- +', '-')
    n = n.replace('+ +', '+')
    n = n.replace('- -', '+')
    n = n.replace('* +', '*')
    n = n.replace('% +', '%')
    n = n.replace('/ +', '/')
    n = n.replace(' / / ', ' # ')
    n = n.replace('# +', '# ')

    n = n.split(' ')

    while '' in n:
        for i in range(len(n)):
            if n[i] == '':
                n.pop(i)
                break

    return n


def error_bad_input(n: list[str]) -> Union[bool, tuple[list[str], bool]]:
    """
    функция проверяет, что между всеми числами есть операнд, что операнды не стоят в конце/начале сроки и обрабатывает унарный знак в начале строки
    :param n: массив n
    :return: либо True (значит ошибка), либо массив без унарного знака в начале и true/false (есть унарный знак в начале строки/нет)
    """
    k: int = 0
    unar: bool = False

    for m in n:
        if is_float(m) and k == 0:
            k = 1
        elif is_float(m) and k == 1:
            return True
        if m in all_operands:
            k = 0

    if n[0] in '*/#%' or n[-1] in all_operands:
        return 1

    elif n[0] == '-':
        n.pop(0)
        unar = True

    elif n[0] == '+':
        n.pop(0)

    return n, unar


def error_0(n: list[str], i: int) -> bool:
    """
    функция проверяет является ли следующий элемент 0, для проверки происходит ли деление/взяие остатка на 0
    :param n: массив n
    :param i: индекс знака (/#%)
    :return: либо True (все ок), либо False (ошибка)
    """
    if i + 1 < len(n):
        if n[i + 1] == '0':
            return False
    return True


def error_bad_digit(digit: float) -> bool:
    """
    функция проверяет, является ли число int
    :param digit: число (в моем случае stek[-1])
    :return: либо True (все ок), либо False (плакиплаки)
    """
    return digit % 1 == 0


def count(n: list[str]) -> Union[None, tuple[list[float], list[str]]]:
    """
    Функция выполняет */#%, закидывает в два стека чисел и операций (+-), также вызывает проверку деления на 0 и %,// над float
    :param n: массив n
    :return:  stek - массив чисел, operation - массив операций (+-) или ошибку (при делении на ноль)
    """
    stek: list[float] = []
    operation: list[str] = []
    slovar = {'*': multiplyy, '/': divisionn, '%': procent, '#': integer_division}

    for i in range(len(n)):
        if i < len(n):
            if n[i][-1] == '.':
                return 'not digit'

            if is_float(n[i]):
                stek.append(float(n[i]))

            elif n[i] in '+-':
                operation.append(n[i])

            else:
                result = slovar[n[i]](stek, n, i)
                if result == 'zero':
                    return 'zero'
                elif result == 'not int':
                    return 'not int'
                elif result == 'bad input':
                    return 'bad input'
                else:
                    stek, n = result
        else:
            break

    return stek, operation


def calculate(n: str) -> float | None:
    """
    в этой функции вызываются все остальные в нужном порядке и подсчитывается итоговый результат
    :param n: введенная пользователем строка n
    :return:  либо ошибку, либо ans - ответ
    """

    if error_extraneous(n) == True:
        raise ExtraneousError('ПОСТОРОННИЕ СИМВОЛЫ')

    if error_empty_input(n) == True:
        raise EmptyError('ПУСТОЙ ВВОД')

    n = edit(n)

    if error_joint_operands(n) == True:
        raise JointOperandsError('СТЫК ОПЕРАНДОВ')

    n = edit_2(n)

    err = error_bad_input(n)

    if err == True:
        raise BadInputError('НЕККОРЕКТНЫЙ ВВОД')
    else:
        n = error_bad_input(n)[0]
        unar = err[1]

    st_op = count(n)

    if st_op == 1:
        raise ZeroDivisionError('Я ВСЕ БИТЮКОВУ РАССКАЖУ')

    elif st_op == 'not int':
        raise BadDigit('НЕЛЬЗЯ ПРОВОДИТЬ ОПЕРАЦИИ //,% НАД FLOAT')
    elif st_op == 'zero':
        raise BadInputError('НЕККОРЕКТНЫЙ ВВОД')
    elif st_op == 'not digit':
        raise NotDigitError('НЕПРАВИЛЬНЫЙ ВВОД ВЕЩЕСТВЕННОГО ЧИСЛА')
    elif st_op == 'bad input':
        raise BadInputError('НЕККОРЕКТНЫЙ ВВОД')
    else:
        if unar == True:
            st_op[0][0] *= -1

        ans: float = st_op[0][0]

        for i in range(1, len(st_op[0])):
            if st_op[1][i - 1] == '+':
                ans += st_op[0][i]
            else:
                ans -= st_op[0][i]
        return ans
