#задание 1
"""
from datetime import datetime

data = {
    "username":"Ivan",
    "created_at": datetime.now().isoformat()
}

import json
json.dumps(data)

data2 =["phyton","api","json"]
json.dumps(data2)
class DB_CONN:
    def __init__(self):
        pass

class User:
    def __init__(self, username,pasword):
        self.username = username
        self.__pasword = self.__hash__()       
        self.__db_session = DB_CONN()
        self.created_at = datetime.now()
    def to_dict(self):
        return {"username":self.username,
                "create_at":self.created_at.isoformat()}
    
user = User("ivan", "secret")


with open("user_data.json","w",encoding="utf-8")as json_file:
          json.dump(user.to_dict(), json_file)
"""
#задания 1-3 ООП
#1
"""
class Employee:
    company = "MyCompany"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"Employee: {self.name}, Salary: {self.salary}, Company: {Employee.company}"


e1 = Employee("Ivan", 5000)
e2 = Employee("Anna", 6000)

print(e1.get_info())
print(e2.get_info())
"""
#2
"""
class Point:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Coordinates must be numbers")
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Coordinates must be numbers")
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


p = Point(3, 4)
print(p.get_coords())

p.set_coords(10, 20)
print(p.get_coords())
"""
#3
"""
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        for p in self.products:
            if p.name == product.name:
                p.quantity += product.quantity
                return
        self.products.append(product)

    def remove_product(self, name, quantity=1):
        for p in self.products:
            if p.name == name:
                if p.quantity > quantity:
                    p.quantity -= quantity
                else:
                    self.products.remove(p)
                return
        print("Товар не найден")

    def get_total(self):
        total = 0
        for p in self.products:
            total += p.price * p.quantity
        return total

    def list(self):
        return list(self.products)

cart = ShoppingCart()
cart.add_product(Product("бананы", 100, 2))
cart.add_product(Product("Хлеб", 50, 1))
cart.add_product(Product("Яблоки", 100, 3)) 
cart.remove_product("Яблоки", 2)

for item in cart.list():
    print(item.name, item.price, item.quantity)

print("Общая сумма:", cart.get_total())
"""


class ServerAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def save_summary(self, summary_text, filename):
        pass

    def get_user_summaries(self):
        pass

    def get_summary(self, summary_id):
        pass

    def delete_summary(self, summary_id):
        pass

    def chat_with_ai_server(self, model: str, message: str, context_id: str | None = None):
        """
        Общение с ИИ через сервер и выбор модели
        model — например: "gpt-5o", "claude-4-5-sonnet", "gemini-3.5-pro", 
                         "deepseek-chat", "llama-3.1-70b" и т.д.
        """
        {"model": model,"message": message,"context_id": context_id}
        pass

    def upload_image(self, image_file):
        # Загрузка изображения на сервер
        pass