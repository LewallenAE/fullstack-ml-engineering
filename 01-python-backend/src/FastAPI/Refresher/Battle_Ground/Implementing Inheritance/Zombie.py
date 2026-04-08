from Enemy import *
import random

class Zombie(Enemy):

    def __init__(self, health_points: int, attack_damage: int) -> None:

        super().__init__(type_of_enemy="Zombie", health_points=health_points, attack_damage=attack_damage)


    def talk(self) -> None:
        print('Grr..Yahhhh *Grumbling* grble. Braiiiins....')

    def walk(self) -> None:
        print("The Zombie shuffles forward")

    def spread_disease(self) -> None:
        print("Zombie has casted contagion, it's trying to spread infection!")

    # def get_type_of_enemy(self) -> str:
        # return self.type_of_enemy

    def special_attack(self) -> None:
        did_special_attack_work = random.random() <= 0.50
        if did_special_attack_work:
            self.health_points += 20
            print("The zombie drains life-force from braaaaaaains regenerating 20 HP")
