import weapons
import chests

stone = weapons.Sword()
rock = weapons.Weapon(100, 101, 10)

print(stone.durability)

stone.use()

print(stone.durability)
