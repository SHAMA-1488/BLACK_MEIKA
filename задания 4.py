#Наследования классов ООП
"""
#1
class Geom(object):
    name = "geom"
    def __init__(self,x1,y1,x2,y2,):
        print(f"init GEOM for {self.__class__}")
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
    def draw(self):
        print("рисование примитива")
    def _verify_coords(self,coord):
        return 0<=coord<=100

class Line(Geom):
    def draw(self):
        print("рисование line")

class Rect(Geom):
     def __init__(self,x1,y1,x2,y2,fill=None):
       super().__init__(x1,y1,x2,y2)
       super()._verify_coords(x1)
       print("рисование recct")
       self.__fill = fill
     def get_coords(self, name):
      return(self.__x1, self.__y1)


class Vector(list):
    def __str__(self):
        return " ".join(map(str,self))
    
r= Rect(0,0,10,10)
print(r.__dict__)
print(r.get_coords())
"""
#2
"""
class Geom2:
    def get_pr(self):
        raise NotImplementedError('В дочернем классе должен быть get_pr()!')

class Rectangle(Geom2):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2*(self.w + self.h)

class Square(Geom2):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return self.a * 4

class Triangle(Geom2):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

r1 = Rectangle(1, 2)
r2 = Rectangle(2, 2)

print(r1.get_pr(), r2.get_pr())

s1 = Square(10)
s2 = Square(30)

print(r1.get_pr(), r2.get_pr())

geom = [r1, r1, s1, s2, Triangle(1, 32, 5)]

for g in geom:
    print(g.get_pr())  # Перебираем вызовы методов в цикле for, полиморфизм
"""
#3
"""
class mixilog2:
    def __init__(self,p1,p2):
        super().__init__()
        print("init mixin2")
class mixilog:
    ID = 0
    def __init__(self):
        print("mixin")
        self.ID += 1
        self.id = self.ID
    def save_sell_log(self):
        print((f"Товар {self.id} продан"))
        
class goods:
    def __init__(self, name, weight, price):
        super().__init__(1)
        print("init mixilog")
        self.name = name
        self.weight = weight
        self.price = price
    def print_info(self):
        print(f"{self.name},{self.weight}, {self.price}")
    
class notebook(mixilog, goods):
    def print_info(self):
        mixilog.print_info(self)
"""
#4
"""
import timeit
class point:
    max_coords = 100
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calc(self):
        self.x += 1
        del self.y
        self.y = 0

class point2d:
    __slots__ = ("x","y","__leight")
    max_coords = 100
    def __init__(self, x, y):
         self.x = x
         self.y = y
         self.leight = (x*x + y*y) ** 0,5
    def calc(self):
        self.x += 1
        del self.y
        self.y = 0
    @property
    def leight(self, vaule):
        return self.__leight
    @leight.setter
    def leight(self, vaule):
        self.__leight = vaule
class point3d(point2d):
    __slots__ = ("z")
    def __init__(self, x, y,z):
        super().__init__(x, y)
        self.z = z
pt3 = point3d(1000, 1000, 1000)
pt3.z = 3000
"""
# задания 1-4
#1
"""
class Payment:
    def pay(self, amount):
        raise NotImplementedError("Метод должен быть переопределен")

class SberPay(Payment):
    def pay(self, amount):
        print(f"Оплата {amount} через Сбер")

class TinkoffPay(Payment):
    def pay(self, amount):
        print(f"Оплата {amount} через Тинькофф")

methods = [SberPay(), TinkoffPay()]
for method in methods:
    method.pay(10000)
"""
#2
"""
class Phone:
    def call(self, number):
        print(f"Звонок на номер {number}")

class Camera:
    def take_photo(self):
        print("Фото сделано")

class Smartphone(Phone, Camera):
    pass

sp = Smartphone()
sp.call("+123456789")   
sp.take_photo()          
print(Smartphone.__mro__)
"""
#3
"""
class Point2D:
    __slots__ = ('x', 'y', 'color') 
    def __init__(self, x, y):
        self.x = x
        self.y = y

pt = Point2D(10, 20)
print(f"Начальные координаты: x={pt.x}, y={pt.y}")

try:
    pt.color = "red"
except AttributeError as e:
    print(f"Ошибка: {e}")
"""
#4
"""
class Point2D:
    __slots__ = ('x', 'y', 'color')
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def length(self):
        return self.x + self.y

class Point3D(Point2D):
    __slots__ = ('z',)
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    @property
    def length(self):
        return self.x + self.y + self.z

pt3 = Point3D(1, 2, 3)
print(f"Точка 3D: x={pt3.x}, y={pt3.y}, z={pt3.z}")
print("Длина (length):", pt3.length)

print("Можно ли добавить новое поле pt3.color?")
try:
    pt3.color = "blue"
except AttributeError as e:
    print("Ошибка:", e)
"""