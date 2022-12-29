"""
Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти, оптимизировать,
вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться.
Описания нужно делать в виде docstrings
"""

from memory_profiler import profile


@profile
def decimal_to_binary():
    user_number = 45
    binary = []
    while user_number > 1:
        binary.insert(0, user_number % 2)
        user_number //= 2
    binary.insert(0, user_number)
    print(binary)


@profile
def decimal_to_binary_m():
    import gc
    gc.disable()
    user_number = 45
    binary = []
    while user_number > 1:
        binary.insert(0, user_number % 2)
        user_number //= 2
    binary.insert(0, user_number)
    del user_number
    print(binary)
    obj = gc.collect()
    print(obj)


decimal_to_binary()


decimal_to_binary_m()


"""
Я выбрал неудачный скрипт для данного задания и не до конца разобрался с оптимизацией памяти.
В данном примере я не увидел разницы по памяти.
Отправлю сейчас задание, так как дедлайн. Если назначите пересдачу, доработаю второе задание.
"""