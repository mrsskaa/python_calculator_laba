from src.calculator_E3 import calculate


def main() -> None:
    """
    Обязательнная составляющая программы. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    n = str(input())
    try:
        print(calculate(n))
    except Exception as error:
        print(error)



if __name__ == "__main__":
    main()
