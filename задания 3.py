
#ООП
"""
class Person:
    S_RUS = 'абвгдеёжзийклмнопрстъьэюя'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, name, old, ps, weight):
        self.verify_fio(fio)

        self.fio = fio.split()

        self.__name = name
        self.__old = old
        self.__ps = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО НЕ СТРОКА')
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Формат неверный")
        letters = cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должна быть хотя бы одна букова")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквы")

    def verify_old(cld, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError(
                'Возраст должен быть в диапозоне [14:120] и быть целым')

    def verify_weight(cld, weight):
        if type(weight) != float and weight < 20:
            raise TypeError('Вес должен быть числом и больше 20')

    def verify_ps(cld, ps):
        if type(ps) != str:
            raise TypeError(
                'Не бывает такого короткого паспорта! >О')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def passport(self):
        return self.__ps

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__ps = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_ps(weight)
        self.__weight = weight

    @old.deleter
    def old(self):
        del self.__old


p = Person('Иван Иванов Иванов', 'Иван', 28, '23424 2342', 70.8)



class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        print(f'__set__: {self.name} = {value}')
        setattr(instance, self.name, value)


class Integer:

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координаты должны быть целыми')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        print(f'__set__: {self.name} = {value}')
        setattr(instance, self.name, value)

class Point3D:
    xr = ReadIntX()
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

p = Point3D(45, 'f', 43)
print(p.x)
p.__dict__['xr'] = 10
print(p.x)
print(p.__dict__)
"""
#Магические методы
#1
"""
class Counter:
    def __init__(self):
        self.__counter = 0
    def __call__(self, step=1, *args, **kwds):
        print("__call__")
        self.__counter += step
        return self.__counter
"""
#2
"""
class StripChars:
     def __init__(self, chars):
        self.__chars = chars
     def __call__(self, *args, **kwds):
         if not isinstance(args[0], str):
             raise ValueError("аргумент должен быть срокой")
         return args[0].strip(self.__chars)
"""
 #3
"""        
class Derivate:
    def __init__(self, func):
        self.__fn = func
    def __call__(self, x, dx = 0.0001,*args, **kwds):
        return(self.__fn(x + dx) - self.__fn(x))/dx
"""
#4
"""
class Cat:
    def __init__(self, name):
        self.__name = name
    def __repr__(self):
        return f"{self.__class__}: {self.__name}"
    def __str__(self):
        return f"{self.__name}"
"""
#5
"""
class Point:
     def __init__(self, *args):
        self.__coords = args
     def __len__(self):
         return len(self.__coords)
     def __abs__(self):
        return list(map(abs,self.__coords)) 
"""
#6
"""
class Clock:
    __DAY = 86400
    def __init__(self, sec, int):
        if not isinstance(sec, int):
            raise TypeError("секунды должны быть целыми")
        self.sec = sec % self.__DAY
    def __add__(self, other):
        if not isinstance(Clock, int):
            return ArithmeticError("Праввый операнд должен быть int или clock")
        sc =other if isinstance(other, int) else other.sec
        return Clock(self.sec+sc)
    def get_time(self):
        s = self.sec % 60
        m = (self.sec // 60) %60
        h = (self.sec // 3600) % 24
        return f"{self.get_formatted(h):{self.get_formatted(m)}}: {self.get_formatted(s)}"
    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2,"0")
"""
#7
"""
class Stud:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)
    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("индекс должен быть целым числом")
        if 0 <= item <= len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")
    def __setitem__(self, key, vaule):
        if not isinstance(key, int) or key < 0:
            raise TypeError("индекс должен быть целым или >0")
        if key>=len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
        self.marks[key] = vaule 
    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("индекс должен быть целым")
        del self.marks[key]

s1 = Stud("Ivan",[5,5,2,2,3,4])
s1 [10] = 5
del s1[3]
print(s1.marks)
"""
#8
"""
class FRange:
    def __init__(self, start=0.0, stop=0.0, step=0.1):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __next__(self):
        if self.value + self.step <= self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

    def __iter__(self):
        self.value = self.start - self.step
        return self
"""
"""
class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=0.1, rows=5):
        self.fr = FRange(start, stop, step)
        self.rows = rows

    def __iter__(self):
        self.value_rows = 0
        return self

    def __next__(self):
        if self.value_rows < self.rows:
            self.value_rows += 1
            return iter(self.fr)
        else:
            raise StopIteration


fr2d = FRange2D(0, 2, 0.5, 4)
for row in fr2d:
    for x in row:
        print(x, end='')
    print()
"""
#задания 1-4

#1
"""
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(";")
        return cls(name, int(age))

user1 = User.from_string("Ivan;41")

print(user1.name,("-"), user1.age)
"""
#2
"""
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("x тип должен быть int или float")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("y тип должен быть int или float")
        self._y = value

p = Coordinate(1, 2)
print(p.x, p.y)
p.x = 5
p.y = 5
print(p.x, p.y)
"""
#3
"""
class Multiplier:
    def __init__(self, n):
        self.n = n

    def __call__(self, value):
        return value * self.n

m = Multiplier(3)

print(m(3))
print(m(5))
"""
#4
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector to Vector")
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only subtract Vector from Vector")
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply Vector by a number")
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __repr__(self):
        return f"({self.x}, {self.y})"
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 7)

v3 = v1 + v2
v4 = v2 - v1
v5 = v1 * 3
v6 = 4 * v2  

print(v3)
print(v4)
print(v5)
print(v6)
"""