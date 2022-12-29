"""
Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени, оптимизировать,
вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться
"""
from timeit import timeit

print(timeit('numbers_in_range_g', 'from skripts import numbers_in_range_g', number=1000000000))
print(timeit('numbers_in_range_m', 'from skripts import numbers_in_range_m', number=1000000000))
print(timeit('numbers_in_range_mm', 'from skripts import numbers_in_range_mm', number=1000000000))
print()
print(timeit('abc_h', 'from skripts import abc_h', number=1000000000))
print(timeit('abc_f', 'from skripts import abc_f', number=1000000000))




"""
При использовании генератора прирост в скорости работы скрипта заметен только при большом количестве исполнений скрипта.
В моем эксперименте это 1 000 000 000 повторений. При числе повторений меньше 10 000 000 "неоптимальный" алгоритм с 
двумя циклами оказывается даже быстрее.

13.112053200020455
13.955937499995343
13.855609199992614

13.816821800020989
13.756902599998284
"""