class Adventurer:
    def __init__(self, name, level, strength, speed, power):
        self.name = name
        self.level = level
        self.strength = strength
        self.speed = speed
        self.power = power
        self.HP = level * 6
        self.hidden = False
    def __repr__(self):
        return f'{self.name} - HP: {self.HP}'
    def attack(self,target):
        if target.hidden == True:
            print(f'{self.name} can\'t see {target.name}')
        else:
            damage = self.strength + 4
            target.HP -= damage
            print(f'{self.name} attacks {target.name} for {damage} damage')

class Thief(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        super().__init__(name, level, strength, speed, power)
        self.HP = level * 8
        self.hidden = True
    def attack(self,target):
        if self.hidden == False:
            super().attack(target)
        else:
            damage = (self.speed + self.level) * 5
            target.HP -= damage
            self.hidden = False
            target.hidden = False
            print(f'{self.name} sneak attacks {target.name} for {damage} damage')

class Mage(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        super().__init__(name, level, strength, speed, power)
        self.fireballs_left = power
    def attack(self,target):
        if self.fireballs_left == 0:
            super().attack(target)
        else:
            damage = self.level * 3
            target.HP -= damage
            target.hidden = False
            self.fireballs_left -= 1
            print(f'{self.name} casts fireball on {target.name} for {damage} damage')

class Ninja(Thief):
    def attack(self,target):
        super().attack(target)
        self.hidden = True
        self.HP += self.level
    
class Wizard(Mage):
    def __init__(self, name, level, strength, speed, power):
        super().__init__(name, level, strength, speed, power)
        self.HP = level * 4
        self.fireballs_left = power * 2

# #Part 1
# thog = Adventurer("Thog",3,5,1,2)
# print(repr(thog))
# goku = Adventurer("Goku",20,10,7,9001)
# print(goku)
# thog.attack(goku)
# print(str(goku))
# print(goku.HP)
# goku.hidden = True
# thog.attack(goku)
# goku.attack(thog)
# print(thog)
# goku.attack(thog)
# print(thog.HP)

# #Part 2
# elizabeth = Thief("Elizabeth",7,2,5,1)
# jack = Thief("Jack",8,3,4,2)
# print(jack)
# print(elizabeth)
# print(elizabeth.hidden)
# print(jack.hidden)
# elizabeth.attack(jack)
# print(jack)
# print(elizabeth.hidden)
# print(jack.hidden)
# jack.attack(elizabeth)
# print(elizabeth)

# #Part 3
# smeagol = Thief("Gollum",11,1,4,1)
# bruce = Ninja("Batman",10,4,5,1)
# print(smeagol)
# print(bruce)
# smeagol.attack(bruce)
# print(smeagol.hidden)
# print(bruce.hidden)
# print(bruce)
# bruce.attack(smeagol)
# print(smeagol.hidden)
# print(bruce.hidden)
# print(bruce)
# smeagol.attack(bruce)
# bruce.attack(smeagol)
# print(smeagol)
# print(bruce)
# print(smeagol.hidden)
# print(bruce.hidden)

# #Part 4
# mario = Mage("Mario",6,1,1,2)
# print(mario.HP)
# print(mario.fireballs_left)
# fox = Ninja("Fox",9,2,4,2)
# print(fox)
# print(fox.hidden)
# mario.attack(fox)
# print(mario.fireballs_left)
# print(fox.hidden)
# print(fox)
# fox.attack(mario)
# print(fox.hidden)
# print(fox)
# mario.attack(fox)
# print(mario.fireballs_left)
# print(fox.hidden)
# fox.attack(mario)
# print(fox.hidden)
# mario.attack(fox)
# fox.attack(mario)

#Part 5
jaina = Mage("Jaina",15,1,2,1)
gandalf = Wizard("Gandalf",13,4,3,1)
print(jaina.fireballs_left)
print(gandalf.fireballs_left)
print(jaina)
print(gandalf)
jaina.attack(gandalf)
gandalf.attack(jaina)
print(jaina.fireballs_left)
print(gandalf.fireballs_left)
print(jaina)
print(gandalf)
jaina.attack(gandalf)
gandalf.attack(jaina)
print(jaina.fireballs_left)
print(gandalf.fireballs_left)
print(jaina)
print(gandalf)
gandalf.attack(jaina)
jaina.attack(gandalf)
print(jaina)
print(gandalf)


