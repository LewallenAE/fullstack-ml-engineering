class ParameterConstructorEnemy:

    def __init__(self, type_of_enemy: str, health_points: int = 10, attack_damage: int = 1) -> None:
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage


        def talk(self):
            print('I am an enemy!')



