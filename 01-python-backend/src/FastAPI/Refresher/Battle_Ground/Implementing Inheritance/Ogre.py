from Enemy import *
import random

class Ogre(Enemy):

    def __init__(self, health_points: int, attack_damage: int) -> None:

        super().__init__(type_of_enemy="Ogre", health_points=health_points, attack_damage=attack_damage)


    def talk(self): -> None:
        print("MMMMmm....Food! Food! Food! Me Eats!")

    def walk(self): -> None:
        print("The ground shakes as the Ogre lumbers forward")

    def attack(self) -> None:
        print("The Ogre's muscles are taught and its swings are heavy")

    def mighty_blow(self) -> None:
        did_special_attack_work = random.random() <= 0.20
