# try:
#     print('start code')
#     print(10 / 0)
#     print(name)
#     print('Ne Errors')
# except NameError:
#     print('We have an error')
# except ZeroDivisionError:
#  print('You can not divide be zero')

# try:
#      print('start code')
#      print(10)
#      print('name')
#      print('Ne Errors')
# except (NameError, ZeroDivisionError):
#      print('We have an error')
# else:
#     print('All is OK')
# finally:
#     print('I work if we have an error or not')
#
# print('Youre code after try-except')


# def checker(value):
#     if type(value) != str:
#         raise TypeError(
#             f'Sorry , we can not work work wiith this type - {type(value)}.'
#             f' We need STR'
#         )
#     else:
#         return value
# try:
#     checker(10)
# except TypeError as error:
#     print(error)
#     print('Try again')
#
# class BuildingError(Exception):
#     def __str__(self):
#         return 'With this naterials we can not build the house'
#
# def check_materials(amount, limit):
#     if amount >= limit:
#         return 'Enough naterials'
#     else:
#         raise BuildingError()
#
# limit = 100
# print(
#     check_materials(80, limit)
# )


import warnings

warnings.simplefilter('always',  SyntaxWarning)
warnings.simplefilter('error',  ImportWarning)


warnings.warn('Warning, no code here', SyntaxWarning)
warnings.warn('Warning, wrong module', ImportWarning)

print(1000)