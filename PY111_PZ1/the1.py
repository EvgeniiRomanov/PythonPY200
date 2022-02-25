

def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    # brackets_open = "("
    # brackets_closed = ")"
    #
    # stack = []                  # стэк для входа-выхода скобок
    # count_in = 0                # счётчик входных скобок
    # count_out = 0               # счётчик выходных скобок
    #
    # for index, elem in enumerate(brackets_row):
    #     if elem in brackets_open:
    #         #count_in += 1
    #         stack.append(elem)
    #         #print(f"Вход: {len(stack)}, {count_in}")
    #         print(f"Вход: {len(stack)}")
    #     if elem in brackets_closed:
    #         #count_out += 1
    #         #print(f"Выходят: {stack}, вх:{count_in}, вых: {count_out}")
    #         print(f"Выходят: {len(stack)}")
    #         if len(stack) == 0:
    #             return False
    #         #elif count_out > count_in:
    #         #    return False
    #         stack.pop()
    #         #if len(stack)
    #         #count_in -= 1
    #         #count_out -= 1
    #
    #     print(f"Прошли шаг - длина: {len(stack)}")
    #     if index == len(brackets_row) - 1:
    #         if len(stack) > 0:
    #             return False
    #
    # return True

    brackets_open = "("
    brackets_closed = ")"

    stack = []                  # стэк для входа-выхода скобок

    for index, elem in enumerate(brackets_row):
        if elem in brackets_open:
            stack.append(elem)
            #print(f"Вход: {len(stack)}")
        if elem in brackets_closed:
            #print(f"Выходят: {len(stack)}")
            if len(stack) == 0:
                return False
            stack.pop()

        #print(f"Прошли шаг - длина: {len(stack)}")
        if index == len(brackets_row) - 1:
            if len(stack) > 0:
                return False

    return True


str_ = "(()"
print(check_brackets(str_))
