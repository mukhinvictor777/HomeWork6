def numbers_in_range_m():
    result = []
    for el in range(20, 240):
        if el % 20 == 0 or el % 21 == 0:
            result.append(el)
    for el in result:
        print(el)


def numbers_in_range_g():
    generator = (el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0)
    for el in generator:
        print(el)


def numbers_in_range_mm():
    result = []
    for el in range(20, 240):
        if el % 20 == 0:
            result.append(el)
        if el % 21 == 0:
            result.append(el)
    for i in range(0, len(result)):
        print(result[i])


def abc_f():
    from itertools import count
    from itertools import cycle

    for i in count(3):
        if i > 10:
            break
        print(i)
    print('')
    text_count = 0
    for item in cycle('ABC'):
        if text_count > 11:
            break
        print(item)
        text_count += 1


def abc_h():
    i = 3
    while i < 11:
        print(i)
        i += 1
    text_count = 11
    text = 'ABC'
    count_cycle = text_count // len(text)
    last_el = text_count % len(text)
    i = 0

    if count_cycle == 0: 
        while i < last_el:
            print(text[i])
            i += 1
    else:
        while i < count_cycle:
            for item in text:
                print(item)
            i += 1
        i = 0
        while i < last_el:
            print(text[i])
            i += 1
