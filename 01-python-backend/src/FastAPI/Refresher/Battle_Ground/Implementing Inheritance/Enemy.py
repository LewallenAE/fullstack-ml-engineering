class Enemy:

    def __init__(self, type_of_enemy:str, health_points: int, attack_damage: int) -> None:
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def appear(self) -> None:
        print(f"A {self.type_of_enemy} approaches.")

    def walk(self) -> None:
        print(f"A {self.type_of_enemy} advances towards you.")

    def talk(self) -> None:
        print(f"{self.type_of_enemy} says: ")

    def status(self) -> None:
        print(f"Foe: {self.type_of_enemy}, HP: {self.health_points}, Attack: {self.attack_damage}")

    def attack(self) -> None:
        print(f"{self.type_of_enemy} swings hard and attacks for {self.attack_damage}!")

