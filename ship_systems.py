import random


def create_ship(name):
    print("Корабль создан")
    return {
        "name": name,
        "health": 100,
        "fuel": 100,
        "shield": 100,
        "weapon": 100,
    }

def ship_status(ship: dict):
    print("Статус корабля")
    for system_name, system_value in ship.items():
        if system_name == "name":
            continue
        system_status = "OK"
        if system_value < 25:
            system_status = "Refusal"
        elif system_value < 50:
            system_status = "Critical"
        elif system_value < 75:
            system_status = "Damaged"
        print(system_name, ":", system_value, "% -", system_status)


def damage_ship(ship: dict, **hits):
    for system_name, damage_value in hits.items():
        if system_name in ship.keys():
            system_value = ship.get(system_name)
            new_value = system_value - damage_value
            if new_value < 0:
                new_value = 0
            ship.update({system_name: new_value})
    print("Корабль поврежден")
    return ship


def ship_test(hit_count: int = 10, max_damage: int = 100):
    ship_1 = create_ship("ArtemShip")
    damage_count = 0
    for i in range(hit_count):
        ship_1 = damage_ship(ship=ship_1, **{
            "health": random.randint(1, max_damage),
            "fuel": random.randint(1, max_damage),
            "shield": random.randint(1, max_damage),
            "weapon": random.randint(1, max_damage),
        })
        ship_status(ship=ship_1)
        if sum([system_value for system_value in ship_1.values() if isinstance(system_value, int)]) == 0:
            return damage_count
        damage_count = i + 1
    return damage_count


def test_mean(test_count: int = 100):
    for d in range(1, 10):
        damage = d * 10
        mean_value = sum([
            ship_test(hit_count=100, max_damage=damage) for _ in range(test_count)
        ]) // test_count
        print(f"Для уничтожения корабля с максимальным уроном {damage} за удар необходимо в среднем {1 + mean_value} ударов")


if __name__ == '__main__':
    ship_test(10, 10)
