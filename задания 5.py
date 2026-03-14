#вложенные классы
#1
from dataclasses import dataclass, field, InitVar, make_dataclass
from pprint import pprint
from typing import Optional
#class 1
"""
class Man:
    title="объект класса для title"
    photo="объект класса для photo"
    ordering = "объект класса для ordering"
    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + "@"+psw)
    class Meta:
        ordering = {'id'}
        def __init__(self, acces):
            self._acces = acces
class point:
    MAX_COORD=100
    MIN_COORD=0
class b1: pass
class b2: pass
def metod1(self):
        print(self.__dict__)
a = type("point",(b1,b2),{"MAX_COORD":100, "MIN_COORD":0, "metod1":metod1, "metod2":lambda self:self.MAX_COORD})
def create_class_point(name, base, attrs):
     attrs.update({"MAX_COORD":100, "MIN_COORD":0})
     return type(name, base, attrs)
class point2(metaclass=create_class_point):
     def get_coords(self):
          return(0,0)
class Meta(type):
     def __init__(cls, name, base, attrs):
        super().__init__(name,base,attrs)
        cls.MAX_COORD = 100
        cls.MIN_COORD = 0
     def __new__(cls, name_class, base, attrs):
          attrs.update({"MAX_COORD":100, "MIN_COORD":0})
          return type.__new__(cls, name_class, base, attrs)
class point3(metaclass=Meta):
     def get_coords(self):
          return(0,0)
class Meta2(type):

    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name_class, base, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs
"""
      
# class 2
"""
class thing:
     def __init__(self,name,weight,price, dims = []):
          self.name = name
          self.weight = weight
          self.price = price
     def __repr__(self):
          return f"thing:{self.__dict__}"
@dataclass
class thingData:
     name:str
     weight:int
     price:float = 0
     dims: list = field(default_factory=list)
     def __eq__(self, other):
          return self.weight == other.weight
     

class Vector3D:
     def __init__(self,x: int,y:int,z:int,calc_len:bool = True):
          self.x = x
          self.y = y
          self.z = z
          self.leight = (x*x+y*y+z*z)**0,5 if calc_len else 0
@dataclass(eq=True, order= False)
class V3D:
     x:int =field(repr=False)
     y:int 
     z:int = field(compare=False)
     calc_len: InitVar[bool] = True
     lenght:float = field(init=False, compare=False, default=0)
     def __post_init__(self,calc_len:bool):
          if calc_len:
            self.lenght = (self.x*self.x+self.y*self.y+self.z*self.z) ** 0.5
 """   

#class 3
"""
class GoodsMethodsFactory:
    @staticmethod
    def get_init_measure():
        return [0, 0, 0]

@dataclass
class Goods:
    current_uid = 0
    uid: int = field(init=False)
    price: any = None
    weight: any = None

    def __post_init__(self):
        print('Goods_post_init')
        Goods.current_uid += 1
        self.uid = Goods.current_uid

   # def __init__(self, uid: Any, price: Any = None, weight: Any = None):


@dataclass
class Book(Goods):
    # def __init__(self, uid: Any, price: float = 0, weight: int | float = 0, title: str = '', author: str = '')

    title: str = ''
    author: str = ''
    price: float = 0
    weight: int | float = 0
    measure: list = field(
        default_factory=GoodsMethodsFactory.get_init_measure())

    def __post_init__(self):
        print('Books_post_init')
        super().__post_init__()


class Car:
    def __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed


CarData = make_dataclass('CarData', [('model', str), 'max_speed', ('price', float, field(
    default=0))], namespace={'get_max_speed': lambda self: self.max_speed})
"""

#СУПЕР ЗАДАНИЕ 4х
from dataclasses import dataclass, asdict
import json

@dataclass
class User:
    name: str = ""
    age: int = 0
    email: str = ""
    id: Optional[int] = None

@dataclass(frozen=True)
class Transaction:
    from_account: str
    to_account: str
    amount: float

class MemoryDB:
    def __init__(self):
        self.users_storage = []
        self.transactions_storage = []
        self._user_id_counter = 1

    def insert_user(self, user_obj):
        user_obj.id = self._user_id_counter
        self._user_id_counter += 1
        self.users_storage.append(user_obj)
        return user_obj

    def filter_users(self, **kwargs):
        result = []
        for user in self.users_storage:
            if all(getattr(user, key, None) == value for key, value in kwargs.items()):
                result.append(user)
        return result

    def save_to_json(self, filename="bank_db.json"):

        data = {"users": [asdict(user) for user in self.users_storage],"transactions": [asdict(t) for t in self.transactions_storage]}
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        

db = MemoryDB()

u1 = User(name="sanek", age=30, email="six-seven@mail.com")
u2 = User(name="mrGIGA", age=25, email="niga@mail.com")
u3 = User(name="Mogger", age=40, email="chopped@mail.com")
print(u1 == u2)
db.insert_user(u1)
db.insert_user(u2)
db.insert_user(u3)

print("Users in DB:")
for user in db.users_storage:
    print(user)

t1 = Transaction("sanek", "mrGIGA", 67.67)
t2 = Transaction("mrGIGA", "Mogger", 1488.88)
t3 = Transaction("Mogger", "sanek", 52.52)

db.transactions_storage.append(t1)
db.transactions_storage.append(t2)
db.transactions_storage.append(t3)

print("\nTransactions:")
print(t1)
print(t2)
print(t3)

print("\nname='sanek', age=30 " "||" "name='Mogger', age=40:")
print(db.filter_users(name="sanek", age=30))
print(db.filter_users(name="Mogger", age=40))

db.save_to_json("asdf.json")