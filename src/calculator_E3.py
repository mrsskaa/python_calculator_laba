from src.errrors import *
def error_extraneous(n):
    """
    функция проверяет строку на посторонние символы
    :param n: входная строка
    :return: либо 1 (ошибка), либо 0 (который означает, что все ок)
    """
    for i in n:
        if not(i.isnumeric()) and i not in '-+*/%# ':
            return 1

    return 0

def error_empty_input(n):
    """
    функция проверяет пустоту ввода
    :param n: входная строка n
    :return: либо 1 (ошибка), либо 0 (который означает, что все ок)
    """
    k = 0

    if len(n) == 0:
        return 1

    for i in n:
        if i != ' ':
            k += 1

    if k == 0:
        return 1

    return 0

def edit(n):
    """
    функция преобразовывает n: выделяет операнды пробелами, убирает лишние пробелы
    :param n: входная строка
    :return: отредактированная строка
    """
    n = n.replace('+', ' + ')
    n = n.replace('-', ' - ')
    n = n.replace('*', ' * ')
    n = n.replace('/', ' / ')
    n = n.replace('%', ' % ')

    while '  ' in n:
        n = n.replace('  ', ' ')

    if n[0] == ' ':
        n = n[1:]

    return n


def error_joint_operands(n):
    """
    функция проверяет на наличие стыка операндов в строке
    :param n: отредактированная строка n
    :return: либо 1 (ошибка), либо 0 (который означает, что все ок)
    """
    if '- *' in n or '- /' in n or '- %' in n or '- #' in n or '+ *' in n or '+ /' in n or '+ %' in n or '+ #' in n or '* *' in n or '# #' in n or '% %' in n or '% /' in n or '% *' in n or '% #' in n or '/ *' in n or '/ #' in n or '/ %' in n or '* /' in n or '* %' in n or '* #' in n or '# *' in n or '# /' in n or '# %' in n:
        return 1

    if n[0:3] == '- -' or n[0:3] == '+ +' or n[0:3] == '+ -' or n[0:3] == '- +':
        return 1

    k = 0
    for i in n:
        if k == 3:
            return 1
        if i.isnumeric():
            k = 0
        elif i != ' ':
            k += 1

    return 0


def edit_2(n):
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


def error_bad_input(n):
    """
    функция проверяет, что между всеми числами есть операнд, что операнды не стоят в конце/начале сроки и обрабатывает унарный знак в начале строки
    :param n: массив n
    :return: либо 1 (значит ошибка), либо массив без унарного знака в начале и true/false (есть унарный знак в начале строки/нет)
    """
    k = 0
    unar = False

    for m in n:
        if m.isnumeric() and k == 0:
            k = 1
        elif m.isnumeric() and k == 1:
            return 1
        if m in '+-/*%#':
            k = 0

    if n[0] in '*/#%' or n[-1] in '*/+-#%':
        return 1

    elif n[0] == '-':
        n.pop(0)
        unar = True

    elif n[0] == '+':
        n.pop(0)

    return n, unar


def error_0(n, i):
    """
    функция проверяет является ли следующий элемент 0, для проверки происходит ли деление/взяие остатка на 0
    :param n: массив n
    :param i: индекс знака (/#%)
    :return: либо 1 (ошибка), либо 0 (который означает, что все ок)
    """
    if n[i + 1] == '0':
        return 1

    return 0


def error_bad_digit(digit):
    """
    функция проверяет, является ли число int
    :param digit: число (в моем случае stek[-1])
    :return: либо 1 (ошибка), либо 0 (который означает, что все ок)
    """
    if digit != float(int(digit)):
        return 1

    return 0


def count(n):
    """
    функция выполняет */#%, закидывает в два стека чисел и операций (+-), также вызывает проверку деления на 0 и %,// над float
    :param n: массив n
    :return:  stek - массив чисел, operation - массив операций (+-) или ошибку (при делении на ноль)
    """
    stek = []
    operation = []

    for i in range(len(n)):
        if i < len(n):
            if n[i].isnumeric():
                stek.append(float(n[i]))


            elif n[i] in '+-':
                operation.append(n[i])

            elif n[i] == '*':
                if n[i+1] == '-':
                    stek.append(float(float(stek[-1]) * float(n[i + 2]) * -1))
                    stek.pop(-2)
                    n.pop(i + 1)
                    n.pop(i + 1)

                else:
                    stek.append(float(float(stek[-1]) * float(n[i + 1])))
                    stek.pop(-2)
                    n.pop(i + 1)


            elif n[i] == '/':
                if error_0(n, i) == 1:
                    return 1

                if n[i+1] == '-':
                    stek.append(float(stek[-1]) / float(n[i + 2]) * -1)
                    stek.pop(-2)
                    n.pop(i + 1)
                    n.pop(i + 1)

                else:
                    stek.append(float(stek[-1]) / float(n[i + 1]))
                    stek.pop(-2)
                    n.pop(i + 1)


            elif n[i] == '#':
                if error_0(n, i) == 1:
                    return 1

                if error_bad_digit(stek[-1]) == 1:
                    return '!'

                if n[i+1] == '-':
                    stek.append(float(int(stek[-1]) // int(n[i + 2]) * -1))
                    stek.pop(-2)
                    n.pop(i + 1)
                    n.pop(i + 1)

                else:
                    stek.append(float(int(stek[-1])) // int(n[i + 1]))
                    stek.pop(-2)
                    n.pop(i + 1)


            elif n[i] == '%':
                if error_0(n, i) == 1:
                    return 0

                if error_bad_digit(stek[-1]) == 1:
                    return '!'

                if n[i+1] == '-':
                    stek.append(float(int(stek[-1]) % (-1*int(n[i + 2]))))
                    stek.pop(-2)
                    n.pop(i + 1)
                    n.pop(i + 1)

                else:
                    stek.append(float(stek[-1]) % int(n[i + 1]))
                    stek.pop(-2)
                    n.pop(i + 1)
        else:
            break

    return stek, operation

def calculate(n):
    """
    в этой функции вызываются все остальные в нужном порядке и подсчитывается итоговый результат
    :param n: введенная пользователем строка n
    :return:  либо ошибку, либо ans - ответ
    """

    if error_extraneous(n) == 1:
        raise ExtraneousError('ПОСТОРОННИЕ СИМВОЛЫ')

    if error_empty_input(n) == 1:
        raise EmptyError('ПУСТОЙ ВВОД')

    n = edit(n)

    if error_joint_operands(n) == 1:
        raise JointOperandsError('СТЫК ОПЕРАНДОВ')

    n = edit_2(n)

    err = error_bad_input(n)

    if err == 1:
        raise BadInputError('НЕККОРЕКТНЫЙ ВВОД')
    else:
        n = error_bad_input(n)[0]
        unar = err[1]



    st_op = count(n)


    if st_op == 1:
        raise ZeroDivisionError('Я ВСЕ БИТЮКОВУ РАССКАЖУ')

    elif st_op == '!':
        raise BadDigit('НЕЛЬЗЯ ПРОВОДИТЬ ОПЕРАЦИИ //,% НАД FLOAT')

    else:
        if unar == True:
            st_op[0][0] *= -1

        ans = st_op[0][0]

        for i in range(1, len(st_op[0])):
            if st_op[1][i - 1] == '+':
                ans += st_op[0][i]
            else:
                ans -= st_op[0][i]
        return ans