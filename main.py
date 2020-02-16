import weapons

stick = weapons.Sword()
potato = weapons.Weapon(10, 10, 10)

print(stick.durability)
print(potato.durability)

stick.use()

print(stick.durability)
