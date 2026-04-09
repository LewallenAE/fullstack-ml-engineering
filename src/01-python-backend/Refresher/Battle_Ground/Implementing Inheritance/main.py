from Enemy import *
from Zombie import *
from Ogre import *
from Hero import *
from Weapon import *

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print('-' * 50)
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemy()},: {e1.health_points} left.")
        print(f"{e2.get_type_of_enemy()}: {e2.health_points} left.")
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage

    print('-' * 50)

    if e1.health_points > 0:
        print(f"{e1.get_type_of_enemy()} wins the battle!")
    else:
        print(f"{e2.get_type_of_enemy()} wins the battle!")


def hero_battle(hero: Hero, enemy: Enemy):
    enemy.talk()

    while hero.health_points > 0 and enemy.health_points > 0:
        print('-' * 50)
        print(f"Jordak,: {hero.health_points} left.")
        print(f"{enemy.get_type_of_enemy()}: {enemy.health_points} left.")
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

    print('-' * 50)

    if hero.health_points > 0:
        print(f"Jordak wins the battle!")
    else:
        print(f"{enemy.get_type_of_enemy()} wins the battle!")


zombie = Zombie(100, 3)
ogre = Ogre(300, 15)


battle(zombie, ogre)

jordak = Hero(100, 1)
weapon = Weapon("Excalibur", ogre.health_points)
jordak.weapon = weapon
jordak.equip_weapon()

hero_battle(jordak, ogre)
