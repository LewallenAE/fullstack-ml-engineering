from Empty_constructor_enemy import *
from Parameter_Constructor_enemy import *
from Private_Enemy import *


enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()

enemy1.type_of_enemy = "Ghoul"

enemy1.talk()
enemy1.walk_forward()
enemy1.attack()

print(f'{enemy1.type_of_enemy} has {enemy1.health_points} health points, and can do {enemy1.attack_damage} amount of damage.')


enemy4 = ParameterConstructorEnemy('Gryphon', 300, 30)

print(f'{enemy4.type_of_enemy} looks extremely strong! It has {enemy4.health_points} health points, and does '
      f'{enemy4.attack_damage} damage.')

elder_vampire = PrivateEnemy('Elder Vampire', 5000, 200)

elder_vampire.set_type_of_enemy("Archaic Elder Vampire") # Tries to reassign but doesn't work because of private variable.

elder_vampire.private_enemy_talk()
elder_vampire.private_enemy_walk()
elder_vampire.private_enemy_attack()
elder_vampire.private_enemy_status()
