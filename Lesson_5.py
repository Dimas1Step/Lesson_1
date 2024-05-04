# import requests
#
# def test_function():
#     pass
#
#
# print(requests.__name__)
# print(requests.__cake__)
#
# print(test_function.__name__)
#
# print(__name__)
#
# x = 10
# print(type(x))
# print(type(requests))
#
# for m in dir():
#     print(m)
#
# print(callable(test_function))
#
# class A:
#     pass
#
# class B(A):
#     pass
#
# print(issubclass(A, B))
# print(issubclass(B, A))
#
# number = 100
# text = 'Hello'
#
# print(isinstance(number, int))
# print(isinstance(number, str))
# print(isinstance(text, str))
# print(isinstance(text, float))
# print(isinstance(text, B))
#
# import inspect
#
# print(inspect.ismodule(requests))
# print(inspect.isclass(A))
# print(inspect.isfunction(test_function))
# print(inspect.getmodule(requests.get))
# print(inspect.getmodule(list))
#
# import sys
#
# print(sys.version)
# print(sys.executable)

import colorama

from colorama import Fore, Back, Style
# функція Fore робить текст іншого кольору
# функція Back замальовую задній фон та по бажанню пише на ньому текст який був заданий у попередній функції Fore


print(Fore.LIGHTBLUE_EX)
print(Back.YELLOW + 'the upper part of the flag of Ukraine')
print(Fore.LIGHTYELLOW_EX)
print(Back.BLUE + 'the lower part of the flag of Ukraine')
print(Fore.GREEN)