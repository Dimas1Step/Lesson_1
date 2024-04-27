# class Human:
#     height = 170
#     gladness = 10
#
# class Student(Human):
#     gladness = 0
#
# class Worker(Human):
#     gladness = 100
#
# nick = Student()
# ann = Worker()
# print(f'Student - {nick.height}, gladess {nick.gladness}')
# print(f'worker - {ann.height}, gladness {ann.gladness}')
#
#

# class GrandParent:
#      height = 170
#      age = 70
#      gladness = 70
#
# class Parent(GrandParent):
#     age = 40
#
# class Child(Parent):
#     height = 110
#     age = 10
#
#     def __init__(self):
#         print(self.age)
#         print(self.height)
#         print(self.gladness)
#
# nick = Child()
#
# class wow:
#     def _hello(self):
#         print('Hello')
#
#     def __wow(self):
#         print('Wow')
#
# x = wow()
# x._hello()
# # x.__wow() ERROR

# class A:
#     hello = 'Hello'
#     _hello = '_Hello'
#     __hello = '__Hello'
#
#     def __init__(self):
#         self.world = 'world'
#         self._world = '_world'
#         self.__world = '__world'
#
#     def printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
#
# class B(A):
#     def printer2(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
#
# B().printer2()

# class Hello:
#     def __init__(self):
#         print('Hello')
#     def not_hello(self):
#         print('NOT')
#
# class World(Hello):
#     def __init__(self):
#         super().__init__()
#         super().not_hello()
#         print('World')
#
# World()

class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.memory = 256
        self.model = model
    def Calculate(self):
        print('Calculating..')

class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = '4k'
    def Display(self):
        print('I display the image on the screen..')

class Smartphone(Display, Computer):
    def print_info(self):
        print(f'memory - {self.memory}')
        print(f'resolution - {self.resolution}')
        print(f'model - {self.model}')

phone = Smartphone(model = 'SuperMax 2000 Ultra_3')
phone.print_info()