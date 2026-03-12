from datetime import datetime
import json

class Astronaut:
    def __init__(self, astronaut_id, name, rank):
        self.astronaut_id = astronaut_id
        self.name = name
        self.rank = rank

    def to_dict(self):
        return {
            "astronaut_id": self.astronaut_id,
            "name": self.name,
            "rank": self.rank
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["astronaut_id"], data["name"], data["rank"])

class Spaceship:
    def __init__(self, ship_id, name, capacity):
        self.ship_id = ship_id
        self.name = name
        self.capacity = capacity

    def to_dict(self):
        return {
            "ship_id": self.ship_id,
            "name": self.name,
            "capacity": self.capacity
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["ship_id"], data["name"], data["capacity"])

class Mission:
    def __init__(self, mission_id, mission_name, spaceship, crew, launch_date):
        self.mission_id = mission_id
        self.mission_name = mission_name
        self.spaceship = spaceship
        self.crew = crew
        self.launch_date = launch_date

    def to_dict(self):
        return {
            "mission_id": self.mission_id,
            "mission_name": self.mission_name,
            "spaceship": self.spaceship.to_dict(),
            "crew": [a.to_dict() for a in self.crew],
            "launch_date": self.launch_date.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        spaceship = Spaceship.from_dict(data["spaceship"])
        crew = [Astronaut.from_dict(a) for a in data["crew"]]
        launch_date = datetime.fromisoformat(data["launch_date"])
        return cls(data["mission_id"], data["mission_name"], spaceship, crew, launch_date)


astro1 = Astronaut(1, "SAKS KECH", "dayn")
astro2 = Astronaut(2, "SMA MACANOV", "dibil")
astro3 = Astronaut(3, "Kirill RAZIK", "Petux")

ship = Spaceship(101, "Orion", 5)

mission = Mission(5001, "MEIKA-Bulki Exploration", ship, [astro1, astro2, astro3], datetime.now())

with open("Osminov_data.json", "w", encoding="utf-8") as file:
    json.dump(mission.to_dict(), file, indent=4, ensure_ascii=False)


with open("Osminov_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

mission = Mission.from_dict(data)

print("Mission:", mission.mission_name)
print("Launch date:", mission.launch_date)
print("Spaceship:", mission.spaceship.name)
print("Crew:")
for astronaut in mission.crew:
    print(astronaut.name, "-", astronaut.rank)

class Medicine:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"], data["quantity"])

class Pharmacy:
    def __init__(self, pharmacy_name, medicines):
        self.pharmacy_name = pharmacy_name
        self.medicines = medicines

    @classmethod
    def from_dict(cls, data):
        medicines = [Medicine.from_dict(m) for m in data["medicines"]]
        return cls(data["pharmacy_name"], medicines)


class PharmacySession:
    def __init__(self, session_id, date, pharmacy):
        self.session_id = session_id
        self.date = date
        self.pharmacy = pharmacy

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["session_id"],
            datetime.fromisoformat(data["date"]),
            Pharmacy.from_dict(data["pharmacy"])
        )


with open("Osminov.json", "r", encoding="utf-8") as f:
    data = json.load(f)

session = PharmacySession.from_dict(data)

print("Pharmacy:", session.pharmacy.pharmacy_name)

print("\nMedicines:")
for m in session.pharmacy.medicines:
    print("-", m.name, "<-> цена:", m.price, "<-> количество:", m.quantity)
