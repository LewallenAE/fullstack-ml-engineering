from Enemy import *

class Zombie(Enemy):

    def __init__(self, health_points: int, attack_damage: int) -> None:

        super().__init__(type_of_enemy="Zombie", health_points=health_points, attack_damage=attack_damage)


    def talk(self) -> None:
        print('Grr..Yahhhh *Grumbling* grble. Braiiiins....')

    def spread_disease(self):
        print("Zombie has casted contagion, it's trying to spread infection!")