class PrivateEnemy:

    def __init__(self, type_of_enemy:str, health_points: int, attack_damage: int) -> None:

        self.__type_of_enemy = type_of_enemy
        self.__health_points = health_points
        self.__attack_damage = attack_damage

    def private_enemy_talk(self) -> None:
        print(f"I am an {self.__type_of_enemy}, prepare for battle!")

    def private_enemy_walk(self) -> None:
        print(f"{self.__type_of_enemy} moves closer to you.")

    def private_enemy_attack(self) -> None:
        print(f"{self.__type_of_enemy} swings hard and attacks you for {self.__attack_damage}")

    def private_enemy_status(self) -> None:
        print(f"Enemy: {self.__type_of_enemy}, HP: {self.__health_points}, Attack Power: {self.__attack_damage}")

    def get_type_of_enemy(self) -> str:
        return self.__type_of_enemy

    def set_type_of_enemy(self, type_of_enemy: str) -> None:
        self.__type_of_enemy = type_of_enemy

    def get_health_points(self) -> int:
        return self.__health_points

    def set_health_points(self, health_points: int) -> None:
        self.__health_points = health_points

    def get_attack_damage(self) -> int:
        return self.__attack_damage

    def set_attack_damage(self, attack_damage: int) -> None:
        self.__attack_damage = attack_damage

